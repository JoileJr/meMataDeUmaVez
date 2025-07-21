from django.views.generic.edit import CreateView,  UpdateView, DeleteView
from django.views.generic.list import ListView
from django.contrib.messages.views import SuccessMessageMixin  # Adicionado

from .models import Endereco, Barbearia, Administrador, Barbeiro, Servico, Cliente, Agendamento, Pagamento

from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin

## Create views ##
class EnderecoListView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('endereco-lista')
    model = Endereco
    template_name = 'listas/endereco.html'
    context_object_name = 'enderecos'
    
    def get_queryset(self):
        return Endereco.objects.filter(usuario=self.request.user)

class EnderecoCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Endereco
    fields = ['rua', 'numero', 'complemento', 'bairro', 'cidade', 'estado', 'cep']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('endereco-lista')
    success_message = "Endereço cadastrado com sucesso!"
    extra_context = {
        "titulo" : "Cadastro de Endereço"
    }
    
    def form_valid(self, form):
        form.instance.usuario = self.request.user
        url_sucesso = super().form_valid(form)
        return url_sucesso
    
class EnderecoUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Endereco
    fields = ['rua', 'numero', 'complemento', 'bairro', 'cidade', 'estado', 'cep']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('endereco-lista')
    success_message = "Endereço atualizado com sucesso!"
    extra_context = {
        "titulo" : "Atualização de Endereço"
    }
    
    def get_queryset(self):
        return Endereco.objects.filter(usuario=self.request.user)
    
class EnderecoDeleteView(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Endereco
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('endereco-lista')
    
    def get_queryset(self):
        return Endereco.objects.filter(usuario=self.request.user)
    
class BarbeariaUpdateView(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Barbearia
    fields = ['nome_fantasia', 'razao_social', 'cnpj', 'telefone', 'email', 'endereco']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('barbearia-lista')
    extra_context = {
        "titulo" : "Atualização de Barbearia"
    }
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['endereco'].queryset = Endereco.objects.filter(usuario=self.request.user)
        return form
    
    def get_queryset(self):
        return Barbearia.objects.filter(usuario=self.request.user)

class BarbeariaCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Barbearia
    fields = ['nome_fantasia', 'razao_social', 'cnpj', 'telefone', 'email', 'endereco'
]
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('barbearia-lista')
    success_message = "Barbearia cadastrada com sucesso!"
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
    success_url = reverse_lazy('barbearia-lista')
    
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
class AdministradorCreateView(SuccessMessageMixin, GroupRequiredMixin, LoginRequiredMixin, CreateView):
    group_required = U"Adminstrador"
    login_url = reverse_lazy('login')
    model = Administrador
    fields = ['nome', 'email', 'telefone', 'cargo', 'barbearia']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')
    success_message = "Administrador cadastrado com sucesso!"
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

class AdministradorUpdateView(SuccessMessageMixin, GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    group_required = U"Adminstrador"
    login_url = reverse_lazy('login')
    model = Administrador
    fields = ['nome', 'email', 'telefone', 'cargo', 'barbearia']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('administrador-lista')
    success_message = "Administrador atualizado com sucesso!"
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
    success_url = reverse_lazy('administrador-lista')
    
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
    
class BarbeiroCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Barbeiro
    fields = ['nome', 'telefone', 'especialidade', 'ativo', 'barbearia']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('barbeiro-lista')
    success_message = "Barbeiro cadastrado com sucesso!"
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

class BarbeiroUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Barbeiro
    fields = ['nome', 'telefone', 'especialidade', 'ativo', 'barbearia']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('barbeiro-lista')
    success_message = "Barbeiro atualizado com sucesso!"
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
    
class ServicoListView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Servico
    template_name = 'listas/servico.html'
    context_object_name = 'servicos'
    
    def get_queryset(self):
        return Servico.objects.filter(usuario=self.request.user)

class ServicoCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Servico
    fields = ['nome', 'descricao', 'preco', 'duracao_minutos', 'barbearia']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('servico-lista')
    success_message = "Serviço cadastrado com sucesso!"
    extra_context = {
        "titulo": "Cadastro de Serviço"
    }

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['barbearia'].queryset = Barbearia.objects.filter(usuario=self.request.user)
        return form

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

class ServicoUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Servico
    fields = ['nome', 'descricao', 'preco', 'duracao_minutos', 'barbearia']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('servico-lista')
    success_message = "Serviço atualizado com sucesso!"
    extra_context = {
        "titulo": "Atualização de Serviço"
    }

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['barbearia'].queryset = Barbearia.objects.filter(usuario=self.request.user)
        return form

    def get_queryset(self):
        return Servico.objects.filter(usuario=self.request.user)
    
class ServicoDeleteView(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Servico
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('servico-lista')
    
    def get_queryset(self):
        return Servico.objects.filter(usuario=self.request.user)
    
class ClienteCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Cliente
    fields = ['nome', 'telefone', 'email', 'data_nascimento']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('cliente-lista')
    success_message = "Cliente cadastrado com sucesso!"
    extra_context = {
        "titulo": "Cadastro de Cliente"
    }

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

class ClienteUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Cliente
    fields = ['nome', 'telefone', 'email', 'data_nascimento']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('cliente-lista')
    success_message = "Cliente atualizado com sucesso!"
    extra_context = {
        "titulo": "Atualização de Cliente"
    }

    def get_queryset(self):
        return Cliente.objects.filter(usuario=self.request.user)

class ClienteDeleteView(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Cliente
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('cliente-lista')
    
    def get_queryset(self):
        return Cliente.objects.filter(usuario=self.request.user)
    
class ClienteListView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Cliente
    template_name = 'listas/cliente.html'
    context_object_name = 'clientes'
    
    def get_queryset(self):
        return Cliente.objects.filter(usuario=self.request.user)

class AgendamentoCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Agendamento
    fields = ['data_hora', 'status', 'observacoes', 'barbearia', 'cliente', 'barbeiro', 'servico']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('agendamento-lista')
    success_message = "Agendamento cadastrado com sucesso!"
    extra_context = {
        "titulo": "Cadastro de Agendamento"
    }

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['barbearia'].queryset = Barbearia.objects.filter(usuario=self.request.user)
        form.fields['cliente'].queryset = Cliente.objects.filter(usuario=self.request.user)
        form.fields['barbeiro'].queryset = Barbeiro.objects.filter(usuario=self.request.user)
        form.fields['servico'].queryset = Servico.objects.filter(usuario=self.request.user)
        return form

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

class AgendamentoUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Agendamento
    fields = ['data_hora', 'status', 'observacoes', 'barbearia', 'cliente', 'barbeiro', 'servico']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('agendamento-lista')
    success_message = "Agendamento atualizado com sucesso!"
    extra_context = {
        "titulo": "Atualização de Agendamento"
    }

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['barbearia'].queryset = Barbearia.objects.filter(usuario=self.request.user)
        form.fields['cliente'].queryset = Cliente.objects.filter(usuario=self.request.user)
        form.fields['barbeiro'].queryset = Barbeiro.objects.filter(usuario=self.request.user)
        form.fields['servico'].queryset = Servico.objects.filter(usuario=self.request.user)
        return form

    def get_queryset(self):
        return Agendamento.objects.filter(usuario=self.request.user)

class AgendamentoDeleteView(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Agendamento
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('agendamento-lista')

    def get_queryset(self):
        return Agendamento.objects.filter(usuario=self.request.user)

class AgendamentoListView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Agendamento
    template_name = 'listas/agendamento.html'
    context_object_name = 'agendamentos'

    def get_queryset(self):
        return Agendamento.objects.filter(usuario=self.request.user)
    
class PagamentoCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Pagamento
    fields = ['valor', 'metodo', 'data_hora', 'agendamento']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('pagamento-lista')
    success_message = "Pagamento cadastrado com sucesso!"
    extra_context = {
        "titulo": "Cadastro de Pagamento"
    }

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['agendamento'].queryset = Agendamento.objects.filter(usuario=self.request.user)
        return form

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

class PagamentoUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Pagamento
    fields = ['valor', 'metodo', 'data_hora', 'agendamento']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('pagamento-lista')
    success_message = "Pagamento atualizado com sucesso!"
    extra_context = {
        "titulo": "Atualização de Pagamento"
    }

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['agendamento'].queryset = Agendamento.objects.filter(usuario=self.request.user)
        return form

    def get_queryset(self):
        return Pagamento.objects.filter(usuario=self.request.user)

class PagamentoDeleteView(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Pagamento
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('pagamento-lista')

    def get_queryset(self):
        return Pagamento.objects.filter(usuario=self.request.user)
    
class PagamentoListView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Pagamento
    template_name = 'listas/pagamento.html'
    context_object_name = 'pagamentos'

    def get_queryset(self):
        return Pagamento.objects.filter(usuario=self.request.user)