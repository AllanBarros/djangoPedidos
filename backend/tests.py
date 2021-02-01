from django.test import TestCase
from .serializers import cashback
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
