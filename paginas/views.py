from django.views.generic import TemplateView

# Create your views here.
class PaginaInicial(TemplateView):
    template_name = "usuario/login2.html"

class MenuView(TemplateView):
    template_name = "paginas/menu.html"

class AvisosView(TemplateView):
    template_name = "paginas/avisos.html"

