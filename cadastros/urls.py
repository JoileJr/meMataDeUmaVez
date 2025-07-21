from django.urls import path

from .views import EnderecoCreateView, BarbeariaCreateView, BarbeariaUpdateView, EnderecoUpdateView, EnderecoDeleteView, BarbeariaDeleteView, BarbeariaListView
from .views import AdministradorCreateView, AdministradorUpdateView, AdministradorDeleteView, AdministradorListView
from .views import BarbeiroCreateView, BarbeiroUpdateView, BarbeiroDeleteView, BarbeiroListView, EnderecoListView
from .views import ServicoListView, ServicoCreateView, ServicoUpdateView, ServicoDeleteView
from .views import ClienteCreateView, ClienteUpdateView, ClienteDeleteView, ClienteListView
from .views import AgendamentoListView, AgendamentoCreateView, AgendamentoUpdateView, AgendamentoDeleteView

urlpatterns = [
    path('cadastrar/endereco/', EnderecoCreateView.as_view(), name='cadastrar-endereco'),
    path('editar/endereco/<int:pk>/', EnderecoUpdateView.as_view(), name='editar-endereco'),
    path('listar/endereco/', EnderecoListView.as_view(), name='endereco-lista' ),
    path('excluir/endereco/<int:pk>/', EnderecoDeleteView.as_view(), name='excluir-endereco'),

    path('excluir/barbearia/<int:pk>/', BarbeariaDeleteView.as_view(), name='excluir-barbearia'),    
    path('cadastrar/barbearia/', BarbeariaCreateView.as_view(), name='cadastrar-barbearia'),
    path('editar/barbearia/<int:pk>/', BarbeariaUpdateView.as_view(), name='editar-barbearia'),
    path('listar/barbearias/', BarbeariaListView.as_view(), name='barbearia-lista' ),
    
    path('cadastrar/administrador/', AdministradorCreateView.as_view(), name='cadastrar-admin'),
    path('editar/administrador/<int:pk>/', AdministradorUpdateView.as_view(), name='editar-admin'),
    path('excluir/administrador/<int:pk>/', AdministradorDeleteView.as_view(), name='excluir-admin'),
    path('listar/administradores/', AdministradorListView.as_view(), name='administrador-lista'),
    
    path('cadastrar/barbeiro/', BarbeiroCreateView.as_view(), name='cadastrar-barbeiro'),
    path('editar/barbeiro/<int:pk>/', BarbeiroUpdateView.as_view(), name='editar-barbeiro'),
    path('excluir/barbeiro/<int:pk>/', BarbeiroDeleteView.as_view(), name='excluir-barbeiro'),
    path('listar/barbeiros/', BarbeiroListView.as_view(), name='barbeiro-lista'),
    
    path('cadastrar/servico/', ServicoCreateView.as_view(), name='cadastrar-servico'),
    path('editar/servico/<int:pk>/', ServicoUpdateView.as_view(), name='editar-servico'),
    path('listar/servicos/', ServicoListView.as_view(), name='servico-lista'),
    path('excluir/servico/<int:pk>/', ServicoDeleteView.as_view(), name='excluir-servico'),
    
    path('cadastrar/cliente/', ClienteCreateView.as_view(), name='cadastrar-cliente'),
    path('editar/cliente/<int:pk>/', ClienteUpdateView.as_view(), name='editar-cliente'),
    path('excluir/cliente/<int:pk>/', ClienteDeleteView.as_view(), name='excluir-cliente'),
    path('listar/clientes/', ClienteListView.as_view(), name='cliente-lista'),
    
    path('cadastrar/agendamento/', AgendamentoCreateView.as_view(), name='cadastrar-agendamento'),
    path('editar/agendamento/<int:pk>/', AgendamentoUpdateView.as_view(), name='editar-agendamento'),
    path('listar/agendamentos/', AgendamentoListView.as_view(), name='agendamento-lista'),
    path('excluir/agendamento/<int:pk>/', AgendamentoDeleteView.as_view(), name='excluir-agendamento'),
]