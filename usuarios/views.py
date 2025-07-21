from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.models import User, Group
from django.urls import reverse_lazy
from .forms import UsuarioForm
from django.shortcuts import get_object_or_404
from .models import Perfil
# Create your views here.
    
class UsuarioCreateView(CreateView):
    template_name = 'usuarios/autocadastro.html'
    form_class = UsuarioForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        grupo = get_object_or_404(Group, name="Adminstrador")
        url = super().form_valid(form)
        self.object.groups.add(grupo)
        self.object.save()

        return url

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Registro de novo usuário"
        context['botao'] = "Cadastrar"

        return context
    
class PerfilUpdate(UpdateView):
    template_name = "usuarios/form.html"
    model = Perfil
    fields = ["nome_completo", "cpf", "telefone"]
    success_url = reverse_lazy("index")

    def get_object(self, queryset=None):
        perfil, created = Perfil.objects.get_or_create(usuario=self.request.user)
        self.object = perfil
        return self.object

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context["titulo"] = "Meus dados pessoais"

        return context