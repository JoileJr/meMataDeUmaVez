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
    
class BarbeariaCreateView(CreateView):
    model = Barbearia
    fields = ['nome_fantasia', 'razao_social', 'cnpj', 'telefone', 'email', 'endereco']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')
    
## Update Views ##
    
class EnderecoUpdateView(UpdateView):
    model = Endereco
    fields = ['rua', 'numero', 'complemento', 'bairro', 'cidade', 'estado', 'cep']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')
    
class BarbeariaUpdateView(UpdateView):
    model = Barbearia
    fields = ['nome_fantasia', 'razao_social', 'cnpj', 'telefone', 'email', 'endereco']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')
        
## Delete Views ##

class EnderecoDeleteView(DeleteView):
    model = Endereco
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('index')

class BarbeariaDeleteView(DeleteView):
    model = Barbearia
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('index')
    
## List Views ##

class BarbeariaListView(ListView):
    model = Barbearia
    template_name = 'listas/barbearia.html'
    context_object_name = 'barbearias'