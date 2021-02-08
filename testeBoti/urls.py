"""testeBoti URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from backend.views import *
from rest_framework_simplejwt import views as jwt_views
# from .views import SignUpView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cadastro-usuario/', CadastroView.as_view()),
    path('validar-login/', jwt_views.TokenObtainPairView.as_view()),
    path('refresh-token/', jwt_views.TokenObtainPairView.as_view()),
    path('cadastro-compra/', PedidoView.as_view()),
    path('listar-compras/', ListarPedidosView.as_view()),
    path('acumulado-cashback/', AcumuladoCashback.as_view()),

]
