from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import LoyaltyProgram, UserLoyaltyPoints
from .serializers import LoyaltyProgramSerializer, UserLoyaltyPointsSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

class LoyaltyProgramViewSet(viewsets.ModelViewSet):
    queryset = LoyaltyProgram.objects.all()
    serializer_class = LoyaltyProgramSerializer
    permission_classes = [permissions.AllowAny]

    @action(detail=True, methods=['post'])
    def buy(self, request, pk=None):
        user = request.user
        program = self.get_object()
        user_points = user.loyalty_points

        if user_points >= program.cost:
            user.loyalty_points -= program.cost
            user.save()
            return Response({'status': 'purchase successful'})
        else:
            return Response({'status': 'not enough points'}, status=status.HTTP_400_BAD_REQUEST)

class UserLoyaltyPointsViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserLoyaltyPointsSerializer
