from django.urls import path
from .views import CVPageView, CVCreateView, get_access_token
from .spotify_utils import login, callback

urlpatterns = [
    path('', CVPageView.as_view(), name='Home'), # Página principal que muestra el CV
    path('create/',CVCreateView.as_view(), name='add'),# Pagina para a;adir pagina web
    path('auth/login/', login, name='spotify_login'),
    path('auth/callback/', callback, name='spotify_callback'),
    path('get-token/', get_access_token, name='get_access_token')
]
