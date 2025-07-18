from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from .views import UsuarioCreateView

urlpatterns = [
    path('login/', LoginView.as_view(template_name='usuarios/login.html'), name='login'),
    path("logout/", LogoutView.as_view(), name="logout"),
    path('cadastro/', UsuarioCreateView.as_view(), name='usuario-cadastro'),
    
    path("alterar-senha/", PasswordChangeView.as_view(
        template_name="usuarios/form.html",
        extra_context={"titulo": "Alterar minha senha"}), name="alterar-senha"),
]