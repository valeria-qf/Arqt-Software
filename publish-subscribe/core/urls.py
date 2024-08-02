from django.urls import path, include
from rest_framework import routers
from core.views import NotificationViewSet, UserSubscriptionViewSet, home

router = routers.DefaultRouter()
router.register(r'user-subscriptions', UserSubscriptionViewSet)
router.register(r'notifications', NotificationViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('', home)
]