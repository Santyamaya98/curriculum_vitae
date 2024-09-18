from django.urls import path
from .views import CVPageView

urlpatterns = [
    path('', CVPageView.as_view(), name='home'),  # Página principal que muestra el CV
]
