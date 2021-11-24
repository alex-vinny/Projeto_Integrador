from django.contrib import admin
from .models import Alunos, Professor, Escola, Notas

# Register your models here.
admin.site.register(Alunos)
admin.site.register(Professor)
admin.site.register(Escola)
admin.site.register(Notas)