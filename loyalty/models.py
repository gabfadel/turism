from django.db import models
from django.conf import settings

class LoyaltyProgram(models.Model):
    title = models.CharField(max_length=255)
    image_url = models.URLField(max_length=200)  # Novo campo para URL da imagem
    cost = models.IntegerField()  # Novo campo para custo em pontos de fidelidade

class UserLoyaltyPoints(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    points = models.IntegerField(default=0)  # Campo para armazenar os pontos de fidelidade do usuário
