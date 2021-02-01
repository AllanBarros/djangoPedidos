from django.shortcuts import render
from rest_framework import generics, permissions
from .models import *
from .serializers import *
import requests
from django.http import JsonResponse

class CadastroView(generics.ListCreateAPIView):
    queryset           = revendedor.objects.all()
    serializer_class   = RevendedorSerializer
    permission_classes = [permissions.AllowAny]


class PedidoView(generics.ListCreateAPIView):
    queryset           = pedido.objects.all()
    serializer_class   = PedidoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ListarPedidosView(generics.ListCreateAPIView):
    
    serializer_class = ListarPedidoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return pedido.objects.filter(cpf_id=self.request.user.cpf)

class AcumuladoCashback(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def get(self, request):
        url = 'https://mdaqk8ek5j.execute-api.us-east-1.amazonaws.com/v1/cashback?'
        headers = { 'Authorization':'Bearer ZXPURQOARHiMc6Y0flhRC1LVlZQVFRnm'}

        r = requests.get(url, params={'cpf':request.user.cpf}, headers=headers)

        return JsonResponse(r.json())