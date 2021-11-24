from django.db import models
from django.db.models.base import Model
from django.contrib.auth.models import User
from django.db.models.deletion import PROTECT
from django.db.models.fields.related import ForeignKey
from django.views.generic.edit import FormView
from django.conf import settings


def user_path(instance, filename):
     return 'usuario_{0}/{1}'.format(instance.user.id, filename)

# Create your models here.
class Escola(models.Model):
    CodEscola = models.CharField(primary_key=True, max_length=5, verbose_name="Código Escola")
    NomeEscola = models.CharField(max_length=50, verbose_name="Nome Escola")
    Endereco = models.CharField(max_length=200, verbose_name="Endereço")
    Bairro = models.CharField(max_length=200)
    Cidade = models.CharField(max_length=100)
    Estado = models.CharField(max_length=50)
    CEP = models.CharField(max_length=20)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return "{} ({})".format(self.NomeEscola, self.CodEscola)

class Professor(models.Model):
    NumRegistro = models.CharField(primary_key=True, max_length=8,  verbose_name='Número Registro Professor')
    CodEscola = models.ForeignKey(Escola, on_delete=PROTECT)
    NomeProf = models.CharField(max_length=50, verbose_name="Nome Professor")
    Materia = models.CharField(max_length=30, verbose_name="Matéria")
    EmailProf = models.CharField(max_length=40, verbose_name="Email Professor")
    SenhaProf = models.CharField(max_length=15,verbose_name="Senha Professor")
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    
    def __str__(self):
        return "{}({}, {})".format(self.NomeProf, self.Materia, self.CodEscola)
    
class Alunos(models.Model):
    RA = models.CharField(primary_key=True, max_length=8)
    CodEscola = models.ForeignKey(Escola, on_delete=PROTECT)
    NomeAluno = models.CharField(max_length=50, verbose_name="Nome Aluno")
    Serie = models.CharField(max_length=5, verbose_name="Série")
    Periodo = models.CharField(max_length=10, verbose_name="Período")
    DataNasci = models.DateField(verbose_name="Data Nascimento")
    Feminino = 'F'
    Masculino = 'M'
    Sexo = [
    ('F','Feminino'),
    ('M','Masculino')
    ]
    Sexo = models.CharField(max_length=2, choices=Sexo)
    EmailAluno = models.CharField(max_length=40, verbose_name="Email Aluno")
    SenhaAluno = models.CharField(max_length=15, null=True, verbose_name="Senha Aluno")
    NomeResp = models.CharField(max_length=50, verbose_name="Nome Responsável")
    GrauParent = models.CharField(max_length=5, verbose_name="Grau de Parentesco")
    TelContato = models.CharField(max_length=15, verbose_name="Telefone de Contato")
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    
    def __str__(self):
        return "{} ({}, {}, {}, {})".format(self.RA, self.NomeAluno, self.CodEscola, self.Serie, self.Periodo)   
    
class Notas(models.Model):
    RA = models.ForeignKey(Alunos, on_delete=PROTECT)
    CodEscola = models.ForeignKey(Escola, on_delete=PROTECT)
    NumRegistro = models.ForeignKey(Professor, on_delete=PROTECT)
    Nota_Ativ1 = models.DecimalField(decimal_places=2, max_digits=4, verbose_name="Atividade 1")
    Nota_P1 = models.DecimalField(decimal_places=2, max_digits=4, verbose_name="Prova 1")
    Nota_Ativ2 = models.DecimalField(decimal_places=2, max_digits=4, verbose_name="Atividade 2")
    Nota_P2 = models.DecimalField(decimal_places=2, max_digits=4,verbose_name="Prova 2")
    Nota_Ativ3 = models.DecimalField(decimal_places=2, max_digits=4,verbose_name="Atividade 3")
    Nota_P3 = models.DecimalField(decimal_places=2, max_digits=4, verbose_name="Prova 3")
    Nota_Ativ4 = models.DecimalField(decimal_places=2, max_digits=4,verbose_name="Atividade 4")
    Nota_P4 = models.DecimalField(decimal_places=2, max_digits=4, verbose_name="Prova 4")
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)


    def Bim_1(self):
        return (((self.Nota_Ativ1)*30)+((self.Nota_P1)*70))/100
        
    def Bim_2(self):
        return (((self.Nota_Ativ2)*30)+((self.Nota_P2)*70))/100
        
    def Bim_3(self):
        return (((self.Nota_Ativ3)*30)+((self.Nota_P3)*70))/100
        
    def Bim_4(self):
        return (((self.Nota_Ativ4)*30)+((self.Nota_P4)*70))/100  
    
    def Media_Final(self):
        return ((((self.Nota_Ativ1+self.Nota_Ativ2+self.Nota_Ativ3+self.Nota_Ativ4)*30)+((self.Nota_P1+self.Nota_P2+self.Nota_P3+self.Nota_P4)*70))/100)/4