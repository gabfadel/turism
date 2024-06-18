from django.urls import path
from .views import UserDetailView, UserUpdateView, UserRedirectView, RegisterView

app_name = "users"
urlpatterns = [
    path("~redirect/", UserRedirectView.as_view(), name="redirect"),
    path("~update/", UserUpdateView.as_view(), name="update"),
    path("<str:username>/", UserDetailView.as_view(), name="detail"),
    path('register/', RegisterView.as_view(), name='register'),
]
