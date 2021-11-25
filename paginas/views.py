from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Avisos
from django.urls import reverse_lazy

# Create your views here.
class PaginaInicial(TemplateView):
    template_name = "usuarios/login2.html"

class MenuView(TemplateView):
    template_name = "paginas/menu.html"


class AvisosCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    group_required = [u"Administrador", u"Professores"]
    login_url= reverse_lazy('login')
    model = Avisos
    fields = ['DataEvento', 'Horario', 'CodEscola', 'Recado']
    template_name = "cadastros/form.html"
    success_url = reverse_lazy('lista-avisos')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['título'] = "Incluir Aviso"
        context['botao'] = "Salvar"
        context['icone'] = '<i class="fa fa-check-square" aria-hidden="true"></i>'

        return context


class AvisosUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    group_required = [u"Administrador", u"Professores"]
    login_url= reverse_lazy('login')
    model = Avisos
    fields = ['DataEvento', 'Horario', 'CodEscola', 'Recado']
    template_name = "cadastros/form.html"
    success_url = reverse_lazy('lista-avisos')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['título'] = "Editar Aviso"
        context['botao'] = "Salvar"
        context['icone'] = '<i class="fa fa-check-square" aria-hidden="true"></i>'

        return context


class AvisosDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    group_required = [u"Administrador", u"Professores"]
    login_url= reverse_lazy('login')
    model = Avisos
    fields = ['DataEvento', 'Horario', 'CodEscola', 'Recado']
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('lista-avisos')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['título'] = "Excluir Aviso"


        return context 


class AvisosList(LoginRequiredMixin, ListView):
    login_url= reverse_lazy('login')
    model = Avisos
    template_name = 'paginas/avisos.html'
    paginate_by=15
    
    def get_queryset(self):

        txt_id = self.request.GET.get('id')
        if txt_id:
            avisos = Avisos.objects.filter(id=txt_id)
        else:
            avisos = Avisos.objects.all()
            
        return avisos

 

