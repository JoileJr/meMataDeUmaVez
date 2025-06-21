from django.urls import path

from .views import IndexView

urlpatterns = [
    # Crie suas urls para as views
    path("", IndexView.as_view(), name="index"),
]