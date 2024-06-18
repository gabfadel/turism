from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView, RedirectView, UpdateView
from django.views import View
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
import json
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    slug_field = "username"
    slug_url_kwarg = "username"

class UserUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = User
    fields = ["name"]
    success_message = _("Information successfully updated")

    def get_success_url(self):
        assert self.request.user.is_authenticated
        return self.request.user.get_absolute_url()

    def get_object(self):
        return self.request.user

class UserRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse("users:detail", kwargs={"username": self.request.user.username})

class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        data = request.data
        username = data.get('username')
        password = data.get('password')
        email = data.get('email')
        if not username or not password or not email:
            return JsonResponse({'error': 'Username, password, and email are required'}, status=400)

        if User.objects.filter(username=username).exists():
            return JsonResponse({'error': 'Username already exists'}, status=400)
