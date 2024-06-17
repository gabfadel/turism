from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LoyaltyProgramViewSet, UserViewSet
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'loyalty_programs', LoyaltyProgramViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls')),  # Adiciona as URLs de autenticação padrão do DRF
    path('auth-token/', obtain_auth_token),  # Endpoint para obter o token de autenticação
]
