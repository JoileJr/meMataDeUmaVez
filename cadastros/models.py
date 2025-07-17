from django.db import models
from django.contrib.auth.models import User

class Endereco(models.Model):
    rua = models.CharField(max_length=255, help_text="Nome da rua do endereço")
    numero = models.CharField(max_length=20, help_text="Número do endereço")
    complemento = models.CharField(max_length=255, blank=True, null=True, help_text="Complemento do endereço (opcional)")
    bairro = models.CharField(max_length=100, help_text="Bairro do endereço")
    cidade = models.CharField(max_length=100, help_text="Cidade do endereço")
    estado = models.CharField(max_length=2, help_text="UF do estado (ex: SP, RJ)")
    cep = models.CharField(max_length=10, help_text="CEP do endereço")
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='usuario_endereco', help_text="Usuário responsável pelo endereço")

    def __str__(self):
        return f"{self.rua}, {self.numero} - {self.bairro}, {self.cidade}/{self.estado}"

class Barbearia(models.Model):
    nome_fantasia = models.CharField(max_length=255, help_text="Nome fantasia da barbearia")
    razao_social = models.CharField(max_length=255, help_text="Razão social da barbearia")
    cnpj = models.CharField(max_length=18, help_text="CNPJ da barbearia")
    telefone = models.CharField(max_length=20, help_text="Telefone de contato da barbearia")
    email = models.EmailField(help_text="E-mail da barbearia")
    endereco = models.OneToOneField(Endereco, on_delete=models.CASCADE, related_name='barbearia', help_text="Endereço da barbearia")
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='usuario_barbearia', help_text="Usuário responsável pela barbearia")

    def __str__(self):
        return self.nome_fantasia

class Administrador(models.Model):
    nome = models.CharField(max_length=255, help_text="Nome do administrador")
    email = models.EmailField(help_text="E-mail do administrador")
    telefone = models.CharField(max_length=20, help_text="Telefone do administrador")
    cargo = models.CharField(max_length=100, help_text="Cargo do administrador")
    barbearia = models.ForeignKey(Barbearia, on_delete=models.CASCADE, related_name='administradores', help_text="Barbearia gerenciada")
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='administrador_usuario', help_text="Usuário responsável pelo administrador")

    def __str__(self):
        return self.nome

class Barbeiro(models.Model):
    nome = models.CharField(max_length=255, help_text="Nome do barbeiro")
    telefone = models.CharField(max_length=20, help_text="Telefone do barbeiro")
    especialidade = models.CharField(max_length=100, help_text="Especialidade do barbeiro")
    ativo = models.BooleanField(default=True, help_text="Indica se o barbeiro está ativo")
    barbearia = models.ForeignKey(Barbearia, on_delete=models.CASCADE, related_name='barbeiros', help_text="Barbearia onde trabalha")
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='barbeiro_usuario', help_text="Usuário responsável pelo barbeiro")

    def __str__(self):
        return self.nome

class Servico(models.Model):
    nome = models.CharField(max_length=255, help_text="Nome do serviço")
    descricao = models.TextField(help_text="Descrição do serviço")
    preco = models.DecimalField(max_digits=8, decimal_places=2, help_text="Preço do serviço")
    duracao_minutos = models.PositiveIntegerField(help_text="Duração do serviço em minutos")
    barbearia = models.ForeignKey(Barbearia, on_delete=models.CASCADE, related_name='servicos', help_text="Barbearia que oferece o serviço")
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='servico_usuario', help_text="Usuário responsável pelo serviço")

    def __str__(self):
        return self.nome

class Cliente(models.Model):
    nome = models.CharField(max_length=255, help_text="Nome do cliente")
    telefone = models.CharField(max_length=20, help_text="Telefone do cliente")
    email = models.EmailField(help_text="E-mail do cliente")
    data_nascimento = models.DateField(help_text="Data de nascimento do cliente")
    created_at = models.DateTimeField(auto_now_add=True, help_text="Data de cadastro do cliente")
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cliente_usuario', help_text="Usuário responsável pelo cliente")

    def __str__(self):
        return self.nome

class Agendamento(models.Model):
    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('confirmado', 'Confirmado'),
        ('cancelado', 'Cancelado'),
        ('concluido', 'Concluído'),
    ]
    data_hora = models.DateTimeField(help_text="Data e hora do agendamento")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pendente', help_text="Status do agendamento")
    observacoes = models.TextField(blank=True, null=True, help_text="Observações do agendamento (opcional)")
    barbearia = models.ForeignKey(Barbearia, on_delete=models.CASCADE, related_name='agendamentos', help_text="Barbearia do agendamento")
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='agendamentos', help_text="Cliente do agendamento")
    barbeiro = models.ForeignKey(Barbeiro, on_delete=models.CASCADE, related_name='agendamentos', help_text="Barbeiro responsável")
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE, related_name='agendamentos', help_text="Serviço agendado")
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='agendamento_usuario', help_text="Usuário responsável pelo agendamento")

    def __str__(self):
        return f"{self.cliente.nome} - {self.data_hora}"

class Pagamento(models.Model):
    valor = models.DecimalField(max_digits=8, decimal_places=2, help_text="Valor do pagamento")
    metodo = models.CharField(max_length=50, help_text="Método de pagamento")
    data_hora = models.DateTimeField(help_text="Data e hora do pagamento")
    agendamento = models.OneToOneField(Agendamento, on_delete=models.CASCADE, related_name='pagamento', null=True, blank=True, help_text="Agendamento relacionado (opcional)")
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pagamento_usuario', help_text="Usuário responsável pelo pagamento")

    def __str__(self):
        return f"Pagamento {self.valor} em {self.data_hora}"