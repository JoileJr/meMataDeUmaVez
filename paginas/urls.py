from django.urls import path

from .views import IndexView, SobreView

urlpatterns = [
    # Crie suas urls para as views
    path("", IndexView.as_view(), name="index"),
    path("sobre", SobreView.as_view(), name="sobre"),
]