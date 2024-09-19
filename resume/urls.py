from django.urls import path
from .views import CVPageView, CVCreateView

urlpatterns = [
    path('', CVPageView.as_view(), name='home'), # Página principal que muestra el CV
      path('create/',CVCreateView.as_view(), name='add')# Pagina para a;adir pagina web
]
