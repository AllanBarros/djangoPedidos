from django.test import TestCase
from .serializers import cashback
from .models import *
# Create your tests here.
class CashbackTestCase(TestCase):
    def test_cashback(self):
        soma_mil = 1000
        soma_dois_mil = 2000
        soma_mil_e_um = 1001

        resultado_soma_mil = cashback(soma_mil)

        resultado_soma_dois_mil = cashback(soma_dois_mil)

        resultado_soma_mil_e_um = cashback(soma_mil_e_um)

        self.assertEqual(resultado_soma_mil['porcentagem_cashback'],'10%')
        self.assertEqual(resultado_soma_dois_mil['porcentagem_cashback'],'20%')
        self.assertEqual(resultado_soma_mil_e_um['porcentagem_cashback'],'15%')

        self.assertEqual(resultado_soma_mil['calculo_cashback'] * soma_mil, 100.0)
        self.assertEqual(resultado_soma_dois_mil['calculo_cashback'] * soma_dois_mil, 400.0)
        self.assertEqual(resultado_soma_mil_e_um['calculo_cashback'] * soma_mil_e_um, 150.15)

class PedidoModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        r = revendedor.objects.create(nome_completo='Allan', cpf='15350946056', email='allan@gmail.com.us', password='123allan')
        pedido.objects.create(codigo='1234', valor=1234, cpf=r)

    def test_list_pedido(self):
        lista = pedido.objects.filter(cpf='15350946056')
        self.assertEqual(len(lista), 1)

    def test_lista_vazia(self):
        lista = pedido.objects.filter(cpf='1234')
        self.assertEqual(len(lista), 0)
    