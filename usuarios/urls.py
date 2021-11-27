from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic.base import View
from .views import UsuarioCreate

urlpatterns = [
    path('', auth_views.LoginView.as_view(
        template_name='usuarios/login2.html'
        ), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('registrar/', UsuarioCreate.as_view(), name='registrar'),
]