from rest_framework import serializers
from loyalty.models import LoyaltyProgram
from django.contrib.auth import get_user_model

User = get_user_model()

class LoyaltyProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoyaltyProgram
        fields = ['id', 'title', 'image_url', 'cost']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'loyalty_points']
        extra_kwargs = {
            'password': {'write_only': True},
            'loyalty_points': {'read_only': True}
        }

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password']
        )
        return user
