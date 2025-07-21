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
    extra_context = {
        "titulo" : "Cadastro de Endereço"
    }
    
    def form_valid(self, form):
        form.instance.usuario = self.request.user
        url_sucesso = super().form_valid(form)
        return url_sucesso
    
class EnderecoUpdateView(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Endereco
    fields = ['rua', 'numero', 'complemento', 'bairro', 'cidade', 'estado', 'cep']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')
    extra_context = {
        "titulo" : "Atualização de Endereço"
    }
    
    def get_queryset(self):
        return Endereco.objects.filter(usuario=self.request.user)
    
class EnderecoDeleteView(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Endereco
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('index')
    
    def get_queryset(self):
        return Endereco.objects.filter(usuario=self.request.user)
    
class BarbeariaUpdateView(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Barbearia
    fields = ['nome_fantasia', 'razao_social', 'cnpj', 'telefone', 'email', 'endereco']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')
    extra_context = {
        "titulo" : "Atualização de Barbearia"
    }
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['endereco'].queryset = Endereco.objects.filter(usuario=self.request.user)
        return form
    
    def get_queryset(self):
        return Barbearia.objects.filter(usuario=self.request.user)

class BarbeariaCreateView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Barbearia
    fields = ['nome_fantasia', 'razao_social', 'cnpj', 'telefone', 'email', 'endereco']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')
    extra_context = {
        "titulo" : "Cadastro de Barbearia"
    }
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['endereco'].queryset = Endereco.objects.filter(usuario=self.request.user)
        return form
    
    def form_valid(self, form):
        form.instance.usuario = self.request.user
        url_sucesso = super().form_valid(form)
        return url_sucesso
    
class BarbeariaDeleteView(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Barbearia
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('index')
    
    def get_queryset(self):
        return Barbearia.objects.filter(usuario=self.request.user)
    
class BarbeariaListView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Barbearia
    template_name = 'listas/barbearia.html'
    context_object_name = 'barbearias'
    
    def get_queryset(self):
        return Barbearia.objects.filter(usuario=self.request.user)
    
## Administrador Views ##
class AdministradorCreateView(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    group_required = U"Adminstrador"
    login_url = reverse_lazy('login')
    model = Administrador
    fields = ['nome', 'email', 'telefone', 'cargo', 'barbearia']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')
    extra_context = {
        "titulo" : "Cadastro de Administrador"
    }
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['barbearia'].queryset = Barbearia.objects.filter(usuario=self.request.user)
        return form
    
    def form_valid(self, form):
        form.instance.usuario = self.request.user
        url_sucesso = super().form_valid(form)
        return url_sucesso

class AdministradorUpdateView(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    group_required = U"Adminstrador"
    login_url = reverse_lazy('login')
    model = Administrador
    fields = ['nome', 'email', 'telefone', 'cargo', 'barbearia']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')
    extra_context = {
        "titulo" : "Atualização de Administrador"
    }
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['barbearia'].queryset = Barbearia.objects.filter(usuario=self.request.user)
        return form
    
    def get_queryset(self):
        return Administrador.objects.filter(usuario=self.request.user)

class AdministradorDeleteView(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    group_required = U"Adminstrador"
    login_url = reverse_lazy('login')
    model = Administrador
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('index')
    
    def get_queryset(self):
        return Administrador.objects.filter(usuario=self.request.user)

class AdministradorListView(GroupRequiredMixin, LoginRequiredMixin, ListView):
    group_required = U"Adminstrador"
    login_url = reverse_lazy('login')
    model = Administrador
    template_name = 'listas/administrador.html'
    context_object_name = 'administradores'
    
    def get_queryset(self):
        return Administrador.objects.filter(usuario=self.request.user)
    
class BarbeiroCreateView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Barbeiro
    fields = ['nome', 'telefone', 'especialidade', 'ativo', 'barbearia']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('barbeiro-lista')
    extra_context = {
        "titulo" : "Cadastro de Barbeiro"
    }

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['barbearia'].queryset = Barbearia.objects.filter(usuario=self.request.user)
        return form

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        url_sucesso = super().form_valid(form)
        return url_sucesso
    
class BarbeiroUpdateView(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Barbeiro
    fields = ['nome', 'telefone', 'especialidade', 'ativo', 'barbearia']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('barbeiro-lista')
    extra_context = {
        "titulo" : "Atualização de Barbeiro"
    }

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['barbearia'].queryset = Barbearia.objects.filter(usuario=self.request.user)
        return form

    def get_queryset(self):
        return Barbeiro.objects.filter(usuario=self.request.user)

class BarbeiroDeleteView(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Barbeiro
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('barbeiro-lista')
    
    def get_queryset(self):
        return Barbeiro.objects.filter(usuario=self.request.user)
    
class BarbeiroListView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Barbeiro
    template_name = 'listas/barbeiro.html'
    context_object_name = 'barbeiros'
    
    def get_queryset(self):
        return Barbeiro.objects.filter(usuario=self.request.user)