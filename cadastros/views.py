from django.utils.translation import templatize
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import Professor, Escola, Alunos, Notas
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin

# CreateView

class ProfessorCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url= reverse_lazy('login')
    group_required = u"Administrador"
    model = Professor
    fields = ['NumRegistro', 'CodEscola', 'NomeProf', 'Materia', 'EmailProf', 'SenhaProf']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('lista-professor')

    def form_valid(self, form):

        form.instance.usuario = self.request.user
        
        url = super().form_valid(form)

        return url

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['título'] = "Cadastro de Professores"
        context['botao'] = "Cadastrar"
        context['icone'] = '<i class="fa fa-book" aria-hidden="true"></i>'
 
        return context

          

class EscolaCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    group_required = u"Administrador"
    login_url= reverse_lazy('login')
    model = Escola
    fields = ['CodEscola','NomeEscola','Endereco', 'Bairro', 'Cidade',  'Estado', 'CEP']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('lista-escola')

    def form_valid(self, form):

        form.instance.usuario = self.request.user
        
        url = super().form_valid(form)

        return url
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['título'] = "Cadastro de Escolas"
        context['botao'] = "Cadastrar"
        context['icone'] = '<i class="fa fa-book" aria-hidden="true"></i>'

        return context   


class AlunoCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    group_required = u"Administrador"
    login_url= reverse_lazy('login')
    model = Alunos
    fields = ['RA', 'CodEscola', 'NomeAluno', 'Serie', 'Periodo', 'DataNasci', 'Sexo', 'EmailAluno', 'SenhaAluno', 'NomeResp', 'GrauParent', 'TelContato']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('lista-alunos')
    
    def form_valid(self, form):

        form.instance.usuario = self.request.user

        url = super().form_valid(form)

        return url

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['título'] = "Cadastro de Alunos"
        context['botao'] = "Cadastrar"
        context['icone'] = '<i class="fa fa-book" aria-hidden="true"></i>'

        return context


class NotasCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    group_required = [u"Administrador", u"Professores"]
    login_url= reverse_lazy('login')
    model = Notas
    fields = ['RA', 'CodEscola', 'NumRegistro', 'Nota_Ativ1', 'Nota_P1','Nota_Ativ2', 'Nota_P2', 'Nota_Ativ3', 'Nota_P3', 'Nota_Ativ4', 'Nota_P4']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('lista-notas')

    def form_valid(self, form):

        form.instance.usuario = self.request.user
        
        url = super().form_valid(form)

        return url
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['título'] = "Cadastro de Notas"
        context['botao'] = "Acicionar Notas"
        context['icone'] = '<i class="fa fa-book" aria-hidden="true"></i>'
        

        return context

#UpdateView

class AlunosUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    group_required = u"Administrador"
    login_url= reverse_lazy('login')
    model = Alunos
    fields = ['RA', 'CodEscola', 'NomeAluno', 'Serie', 'Periodo', 'DataNasci', 'Sexo', 'EmailAluno', 'SenhaAluno', 'NomeResp', 'GrauParent', 'TelContato']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('lista-alunos')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['título'] = "Editar Alunos"
        context['botao'] = "Salvar"
        context['icone'] = '<i class="fa fa-check-square" aria-hidden="true"></i>'
        

        return context

class ProfessorUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    group_required = u"Administrador"
    login_url= reverse_lazy('login')
    model = Professor
    fields = ['NumRegistro', 'CodEscola', 'NomeProf', 'Materia', 'EmailProf', 'SenhaProf']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('lista-professor')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['título'] = "Editar Professores"
        context['botao'] = "Salvar"
        context['icone'] = '<i class="fa fa-check-square" aria-hidden="true"></i>'

        return context

class EscolaUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    group_required = u"Administrador"
    login_url= reverse_lazy('login')
    model = Escola
    fields = ['CodEscola','NomeEscola','Endereco', 'Bairro', 'Cidade',  'Estado', 'CEP']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('lista-escola')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['título'] = "Editar Escolas"
        context['botao'] = "Salvar"
        context['icone'] = '<i class="fa fa-check-square" aria-hidden="true"></i>'

        return context

class NotasUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    group_required = [u"Administrador", u"Professores"]
    login_url= reverse_lazy('login')
    model = Notas
    fields = ['RA', 'CodEscola', 'NumRegistro', 'Nota_Ativ1', 'Nota_P1','Nota_Ativ2', 'Nota_P2', 'Nota_Ativ3', 'Nota_P3', 'Nota_Ativ4', 'Nota_P4']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('lista-notas')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['título'] = "Editar Notas"
        context['botao'] = "Salvar"
        context['icone'] = '<i class="fa fa-check-square" aria-hidden="true"></i>'

        return context

#DeleteView

class AlunosDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    group_required = u"Administrador"
    login_url= reverse_lazy('login')
    model = Alunos
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('lista-alunos')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['título'] = "Excluir Alunos"


        return context 

class ProfessorDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    group_required = u"Administrador"
    login_url= reverse_lazy('login')
    model = Professor
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('lista-professor')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['título'] = "Excluir Professores"

        return context 

class EscolaDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    group_required = u"Administrador"
    login_url= reverse_lazy('login')
    model = Escola
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('lista-escola')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['título'] = "Excluir Escola"
        return context 

class NotasDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    group_required = [u"Administrador", u"Professores"]
    login_url= reverse_lazy('login')
    model = Notas
    fields = ['RA', 'CodEscola', 'NumRegistro', 'Nota_Ativ1', 'Nota_P1','Nota_Ativ2', 'Nota_P2', 'Nota_Ativ3', 'Nota_P3', 'Nota_Ativ4', 'Nota_P4']
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('lista-notas')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['título'] = "Excluir Notas"

        return context 

#ListView

class AlunoList(LoginRequiredMixin, ListView):
    login_url= reverse_lazy('login')
    model = Alunos
    template_name = 'cadastros/aluno.html'
    paginate_by=10

    def get_queryset(self):

        txt_aluno = self.request.GET.get('RA')
        if txt_aluno:
            aluno = Alunos.objects.filter(RA=txt_aluno)
        else:
            aluno = Alunos.objects.all()
            
        return aluno

class ProfessorList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    group_required = u"Administrador"
    login_url= reverse_lazy('login')
    model = Professor
    template_name = 'cadastros/professor.html'
    paginate_by=500

    def get_queryset(self):

        txt_professor = self.request.GET.get('NumRegistro')
        if txt_professor:
            professor = Professor.objects.filter(NumRegistro=txt_professor)
        else:
            professor = Professor.objects.all()
            
        return professor   

class EscolaList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    group_required = u"Administrador"
    login_url= reverse_lazy('login')
    model = Escola
    template_name = 'cadastros/escola.html'
    paginate_by=15

    def get_queryset(self):

        txt_escola = self.request.GET.get('CodEscola')
        if txt_escola:
            escola = Escola.objects.filter(CodEscola=txt_escola)
        else:
            escola = Escola.objects.all()
            
        return escola

class NotasList(LoginRequiredMixin, ListView):
    login_url= reverse_lazy('login')
    model = Notas
    template_name = 'cadastros/notas.html'
    paginate_by=15
    
    def get_queryset(self):

        txt_ra = self.request.GET.get('RA')
        if txt_ra:
            notas = Notas.objects.filter(RA=txt_ra)
        else:
            notas = Notas.objects.all()
            
        return notas

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['Notas'] = Notas.objects.filter(usuario=self.request.user)

        return context 


   ## def get_queryset(self):
   ##   self.object_list = Notas.objects.filter(usuario=self.request.user)
   ##   return self.object_list

   ## def get_objects(self, queryset=None):
   ##   self.object = Notas.objects.get(pk=self.kwargs['pk'])
   ##   return self.object
