from django.urls import path

from .views import EnderecoCreateView, BarbeariaCreateView, BarbeariaUpdateView, EnderecoUpdateView, EnderecoDeleteView, BarbeariaDeleteView, BarbeariaListView
from .views import AdministradorCreateView, AdministradorUpdateView, AdministradorDeleteView, AdministradorListView
from .views import BarbeiroCreateView, BarbeiroUpdateView, BarbeiroDeleteView, BarbeiroListView, EnderecoListView
from .views import ServicoListView, ServicoCreateView, ServicoUpdateView, ServicoDeleteView

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
]