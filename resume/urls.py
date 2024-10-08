from django.urls import path
from .views import CVPageView, CVCreateView
from .spotify_utils import login, callback

urlpatterns = [
    path('', CVPageView.as_view(), name='home'), # Página principal que muestra el CV
    path('create/',CVCreateView.as_view(), name='add'),# Pagina para a;adir pagina web
    path('auth/login/', login, name='spotify_login'),
    path('auth/callback/', callback, name='spotify_callback'),
]
