from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

# Create your models here.
class revendedor(AbstractUser):
    id = models.AutoField(primary_key=True)
    nome_completo = models.CharField(max_length=255)
    cpf = models.CharField(max_length=14, unique=True)
    username = None
    email = models.EmailField(('endereco de email'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

class pedido(models.Model):
    id = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=255)
    valor = models.FloatField()
    data_pedido = models.DateTimeField(auto_now_add=True)
    cpf = models.ForeignKey('revendedor', to_field='cpf',db_column='cpf', on_delete=models.CASCADE)

    def mes_pedido(self):
        return self.data_pedido.strftime('%B')

class statusPedido(models.Model):
    id_status_pedido = models.AutoField(primary_key=True)
    id_pedido = models.ForeignKey('pedido', on_delete=models.PROTECT)
    id_status = models.ForeignKey('status', on_delete=models.PROTECT)
    data = models.DateTimeField(auto_now_add=True)

class status(models.Model):
    id_status = models.AutoField(primary_key=True)
    status = models.CharField(max_length=50, default="Em validação")