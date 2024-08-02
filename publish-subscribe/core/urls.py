from django.urls import path, include
from rest_framework import routers
from core.views import NotificationViewSet, UserSubscriptionViewSet

router = routers.DefaultRouter()
router.register(r'users', UserSubscriptionViewSet, basename='user')
router.register(r'notifications', NotificationViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
