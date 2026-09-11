from rest_framework import generics

from .models import Payment, User
from .serializers import PaymentSerializer, UserSerializer


class UserRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PaymentListAPIView(generics.ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    filterset_fields = ["course", "lesson", "payment_method"]
    ordering_fields = ["payment_date"]
    ordering = ["payment_date"]
