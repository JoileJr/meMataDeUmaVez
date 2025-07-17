from django.views.generic import TemplateView

from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class IndexView(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('login')
    template_name = 'paginas/modelo.html'
    
class SobreView(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('login')
    template_name = 'paginas/sobre.html'