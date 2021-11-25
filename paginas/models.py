from django.db import models



class Avisos(models.Model):
    DataEvento = models.DateField(verbose_name="Data")
    Horario= models.TimeField(verbose_name="Ínicio")
    CodEscola = models.CharField(max_length=5, verbose_name="Código Escola")
    Recado= models.CharField(max_length=300, verbose_name="Aviso")

    def __str__(self):
        return "{} {} - {} : {}".format(self.DataEvento, self.Horario, self.CodEscola, self.Recado)

# Create your models here.
