from django.urls import path

from .views import EnderecoCreateView, BarbeariaCreateView, BarbeariaUpdateView, EnderecoUpdateView, EnderecoDeleteView, BarbeariaDeleteView, BarbeariaListView

urlpatterns = [
    path('cadastrar/endereco/', EnderecoCreateView.as_view(), name='cadastrar-endereco'),
    path('cadastrar/barbearia/', BarbeariaCreateView.as_view(), name='cadastrar-barbearia'),
    
    path('editar/endereco/<int:pk>/', EnderecoUpdateView.as_view(), name='editar-endereco'),
    path('editar/barbearia/<int:pk>/', BarbeariaUpdateView.as_view(), name='editar-barbearia'),
    
    path('excluir/endereco/<int:pk>/', EnderecoDeleteView.as_view(), name='excluir-endereco'),
    path('excluir/barbearia/<int:pk>/', BarbeariaDeleteView.as_view(), name='excluir-barbearia'),
    
    path('listar/barbearias/', BarbeariaListView.as_view(), name='barbearia-list'),
]