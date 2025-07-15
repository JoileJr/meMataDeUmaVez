from django.views.generic.edit import CreateView,  UpdateView, DeleteView
from django.views.generic.list import ListView

from .models import Endereco, Barbearia, Administrador, Barbeiro, Servico, Cliente

from django.urls import reverse_lazy

## Create views ##

class EnderecoCreateView(CreateView):
    model = Endereco
    fields = ['rua', 'numero', 'complemento', 'bairro', 'cidade', 'estado', 'cep']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')
class EnderecoUpdateView(UpdateView):
    model = Endereco
    fields = ['rua', 'numero', 'complemento', 'bairro', 'cidade', 'estado', 'cep']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')
    
class EnderecoDeleteView(DeleteView):
    model = Endereco
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('index')
    
class BarbeariaUpdateView(UpdateView):
    model = Barbearia
    fields = ['nome_fantasia', 'razao_social', 'cnpj', 'telefone', 'email', 'endereco']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

class BarbeariaCreateView(CreateView):
    model = Barbearia
    fields = ['nome_fantasia', 'razao_social', 'cnpj', 'telefone', 'email', 'endereco']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')
    
class BarbeariaDeleteView(DeleteView):
    model = Barbearia
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('index')
    
class BarbeariaListView(ListView):
    model = Barbearia
    template_name = 'listas/barbearia.html'
    context_object_name = 'barbearias'
    
## Administrador Views ##
class AdministradorCreateView(CreateView):
    model = Administrador
    fields = ['nome', 'email', 'telefone', 'cargo', 'barbearia']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

class AdministradorUpdateView(UpdateView):
    model = Administrador
    fields = ['nome', 'email', 'telefone', 'cargo', 'barbearia']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

class AdministradorDeleteView(DeleteView):
    model = Administrador
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('index')

class AdministradorListView(ListView):
    model = Administrador
    template_name = 'listas/administrador.html'
    context_object_name = 'administradores'
    
class BarbeiroCreateView(CreateView):
    model = Barbeiro
    fields = ['nome', 'telefone', 'especialidade', 'ativo', 'barbearia']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('barbeiro-lista')
    
class BarbeiroUpdateView(UpdateView):
    model = Barbeiro
    fields = ['nome', 'telefone', 'especialidade', 'ativo', 'barbearia']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('barbeiro-lista')

class BarbeiroDeleteView(DeleteView):
    model = Barbeiro
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('barbeiro-lista')
    
class BarbeiroListView(ListView):
    model = Barbeiro
    template_name = 'listas/barbeiro.html'
    context_object_name = 'barbeiros'