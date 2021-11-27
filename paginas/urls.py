from django.urls import path
from .views import AvisosCreate, AvisosList, PaginaInicial, MenuView, AvisosDelete, AvisosUpdate

urlpatterns = [
    path('menu/', MenuView.as_view(), name="menu"),
    path('incluir/avisos/', AvisosCreate.as_view(), name="incluir-avisos"),
    path('editar/avisos/<int:pk>/', AvisosUpdate.as_view(), name='editar-avisos'),
    path('excluir/avisos/<int:pk>/', AvisosDelete.as_view(), name='excluir-avisos'),
    path('lista/avisos/', AvisosList.as_view(), name='lista-avisos'),
]