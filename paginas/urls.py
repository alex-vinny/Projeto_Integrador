from django.urls import path
from .views import PaginaInicial, MenuView, AvisosView

urlpatterns = [
    path('', PaginaInicial.as_view(), name="login"),
    path('menu/', MenuView.as_view(), name="menu"),
    path('avisos/', MenuView.as_view(), name="avisos"),
]