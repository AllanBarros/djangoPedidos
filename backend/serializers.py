from rest_framework import serializers
from .models import *
from django.db.models import Sum
from django.db.models.functions import TruncMonth
from django.contrib.auth.hashers import make_password

def cashback(total):
    if total <= 1000:
        return {'porcentagem_cashback':'10%', 'calculo_cashback':0.10} 
    elif total >= 1000 and total <= 1500:
        return {'porcentagem_cashback':'15%', 'calculo_cashback':0.15}
    else:
        return {'porcentagem_cashback':'20%', 'calculo_cashback':0.20}


def calculo_cashback(self, instance):
    
    mes_pedido = instance.data_pedido.month
    ano_pedido = instance.data_pedido.year
    
    total_mes = pedido.objects.annotate(mes=TruncMonth('data_pedido')).filter(mes__month=mes_pedido, mes__year = ano_pedido).values('mes').annotate(Sum('valor')) 
    
    resultado_cashback = cashback(total_mes[0]['valor__sum'])
    
    return resultado_cashback

def set_status(pedido, status):

    sp = statusPedido()
    sp.id_pedido = pedido
    sp.id_status = status
    sp.save()

    return sp


class PedidoSerializer(serializers.ModelSerializer):

    class Meta:
        model = pedido
        fields = [
            'codigo',
            'valor',
            'cpf',
        ]

    def create(self, validated_data):
        
        p = pedido()
        p.codigo = validated_data['codigo']
        p.cpf = revendedor.objects.get(cpf=validated_data['cpf'].cpf)
        p.valor = validated_data['valor']
        p.save()

        if validated_data['cpf'].cpf == '15350946056':
            status_selecionado = status.objects.get(status='Aprovado')
        else:
            status_selecionado = status.objects.get(status='Em validação')

        sp = set_status(p, status_selecionado)

        l = logs()
        l.acao = 'Criação de pedido'
        l.id_revendedor = revendedor.objects.get(cpf=validated_data['cpf'].cpf)
        l.save()
        
        return p


class RevendedorSerializer(serializers.ModelSerializer):

    class Meta:
        model = revendedor
        fields = [
            'nome_completo',
            'cpf',
            'email',
            'password',
    ]

    def validate_password(self, value: str) -> str:
        return make_password(value)

class ListarPedidoSerializer(serializers.ModelSerializer):

    porcentagem_cashback = serializers.SerializerMethodField()
    valor_cashback = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField() 

    class Meta:
        model = pedido
        fields = [
            'codigo',
            'valor',
            'cpf',
            'data_pedido',
            'porcentagem_cashback',
            'valor_cashback',
            'status',
        ]

    def get_porcentagem_cashback(self, instance):

        cashback = calculo_cashback(self, instance)
            
        return cashback['porcentagem_cashback']

    def get_valor_cashback(self, instance):

        cashback = calculo_cashback(self, instance)

        return instance.valor * cashback['calculo_cashback']

    def get_status(self, instance):
        sp = statusPedido.objects.filter(id_pedido=instance.pk).latest('data')
        ultimo_status = sp.id_status.status
        return ultimo_status