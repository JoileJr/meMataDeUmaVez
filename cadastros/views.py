from django.views.generic.edit import CreateView,  UpdateView, DeleteView
from django.views.generic.list import ListView

from .models import Endereco, Barbearia, Administrador, Barbeiro, Servico, Cliente

from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin

## Create views ##

class EnderecoCreateView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Endereco
    fields = ['rua', 'numero', 'complemento', 'bairro', 'cidade', 'estado', 'cep']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')
class EnderecoUpdateView(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Endereco
    fields = ['rua', 'numero', 'complemento', 'bairro', 'cidade', 'estado', 'cep']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')
    
class EnderecoDeleteView(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Endereco
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('index')
    
class BarbeariaUpdateView(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Barbearia
    fields = ['nome_fantasia', 'razao_social', 'cnpj', 'telefone', 'email', 'endereco']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

class BarbeariaCreateView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Barbearia
    fields = ['nome_fantasia', 'razao_social', 'cnpj', 'telefone', 'email', 'endereco']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')
    
class BarbeariaDeleteView(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Barbearia
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('index')
    
class BarbeariaListView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Barbearia
    template_name = 'listas/barbearia.html'
    context_object_name = 'barbearias'
    
## Administrador Views ##
class AdministradorCreateView(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    group_required = U"Adminstrador"
    login_url = reverse_lazy('login')
    model = Administrador
    fields = ['nome', 'email', 'telefone', 'cargo', 'barbearia']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

class AdministradorUpdateView(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    group_required = U"Adminstrador"
    login_url = reverse_lazy('login')
    model = Administrador
    fields = ['nome', 'email', 'telefone', 'cargo', 'barbearia']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

class AdministradorDeleteView(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    group_required = U"Adminstrador"
    login_url = reverse_lazy('login')
    model = Administrador
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('index')

class AdministradorListView(GroupRequiredMixin, LoginRequiredMixin, ListView):
    group_required = U"Adminstrador"
    login_url = reverse_lazy('login')
    model = Administrador
    template_name = 'listas/administrador.html'
    context_object_name = 'administradores'
    
class BarbeiroCreateView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Barbeiro
    fields = ['nome', 'telefone', 'especialidade', 'ativo', 'barbearia']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('barbeiro-lista')
    
class BarbeiroUpdateView(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Barbeiro
    fields = ['nome', 'telefone', 'especialidade', 'ativo', 'barbearia']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('barbeiro-lista')

class BarbeiroDeleteView(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Barbeiro
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('barbeiro-lista')
    
class BarbeiroListView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Barbeiro
    template_name = 'listas/barbeiro.html'
    context_object_name = 'barbeiros'