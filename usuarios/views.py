from django.views.generic.edit import CreateView
from django.contrib.auth.models import User, Group
from .forms import UsuarioForm
from django.urls import reverse_lazy
from braces.views import GroupRequiredMixin
from django.shortcuts import get_object_or_404

# Create your views here.


class UsuarioCreate(CreateView, GroupRequiredMixin):
    template_name = "cadastros/form.html"
    group_required = u"Administrador"
    form_class = UsuarioForm
    success_url = reverse_lazy('logout')

    def form_valid(self, form):
        grupo = get_object_or_404(Group, name="Alunos")

        url =  super().form_valid(form)

        self.object.groups.add(grupo)
        self.object.save()

        return url

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['título'] = "Criar Usuário"
        context['botao'] = "Criar"
        context['icone'] = '<i class="fa fa-book" aria-hidden="true"></i>'

        return context 

