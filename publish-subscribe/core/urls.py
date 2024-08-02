# core/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserSubscriptionViewSet

router = DefaultRouter()
router.register(r'subscriptions', UserSubscriptionViewSet, basename='user-subscription')

urlpatterns = [
    path('', include(router.urls)),
]
