from django.urls import path

from .views import (PaymentListAPIView, UserRegistrationAPIView,
                    UserRetrieveUpdateDestroyAPIView)

urlpatterns = [
    path("register/", UserRegistrationAPIView.as_view(), name="user_register"),
    path(
        "users/<int:pk>/",
        UserRetrieveUpdateDestroyAPIView.as_view(),
        name="user-detail",
    ),
    path("payments/", PaymentListAPIView.as_view(), name="payment-list"),
]
