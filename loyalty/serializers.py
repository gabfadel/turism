from rest_framework import serializers
from .models import LoyaltyProgram, UserLoyaltyPoints
from django.contrib.auth import get_user_model

User = get_user_model()

class LoyaltyProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoyaltyProgram
        fields = ['id', 'title', 'image_url', 'cost']

class UserLoyaltyPointsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserLoyaltyPoints
        fields = ['user', 'points']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
