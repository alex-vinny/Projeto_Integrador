from django.urls import path
from .views import AlunoCreate, ProfessorCreate, EscolaCreate, NotasCreate
from .views import AlunosUpdate, ProfessorUpdate, EscolaUpdate, NotasUpdate
from .views import AlunosDelete, ProfessorDelete, EscolaDelete, NotasDelete
from .views import AlunoList, ProfessorList, EscolaList, NotasList

urlpatterns = [
    path('cadastrar/aluno/', AlunoCreate.as_view(), name="cadastrar-aluno"),
    path('cadastrar/professor/', ProfessorCreate.as_view(), name="cadastrar-professor"),
    path('cadastrar/escola/', EscolaCreate.as_view(), name="cadastrar-escola"),
    path('cadastrar/notas/', NotasCreate.as_view(), name='cadastrar-notas'),

        
    path('editar/alunos/<int:pk>/', AlunosUpdate.as_view(), name='editar-aluno'),
    path('editar/professor/<int:pk>/', ProfessorUpdate.as_view(), name='editar-professor'),
    path('editar/escola/<str:pk>/', EscolaUpdate.as_view(), name='editar-escola'),
    path('editar/notas/<int:pk>', NotasUpdate.as_view(), name='editar-notas'),

    path('excluir/alunos/<int:pk>/', AlunosDelete.as_view(), name='excluir-aluno'),
    path('excluir/professor/<int:pk>/', ProfessorDelete.as_view(), name='excluir-professor'),
    path('excluir/escola/<str:pk>/', EscolaDelete.as_view(), name='excluir-escola'),
    path('excluir/notas/<int:pk>', NotasDelete.as_view(), name='excluir-notas'),

    path('lista/alunos/', AlunoList.as_view(), name='lista-alunos'),
    path('lista/professor/', ProfessorList.as_view(), name='lista-professor'),
    path('lista/escola/', EscolaList.as_view(), name='lista-escola'),
    path('lista/notas/', NotasList.as_view(), name='lista-notas'),
    ]