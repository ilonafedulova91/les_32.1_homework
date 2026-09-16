from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated

from .models import Payment, User
from .permissions import IsSelf
from .serializers import (PaymentSerializer, UserRegistrationSerializer,
                          UserSerializer)


class UserRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAuthenticated, IsSelf]

        return [permission() for permission in permission_classes]


class PaymentListAPIView(generics.ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    filterset_fields = ["course", "lesson", "payment_method"]
    ordering_fields = ["payment_date"]
    ordering = ["payment_date"]


class UserRegistrationAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]
