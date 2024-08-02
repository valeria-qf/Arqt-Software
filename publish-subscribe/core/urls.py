from django.urls import path, include
from rest_framework import routers
from core.views import NotificationViewSet

router = routers.DefaultRouter()

router.register(r'notifications', NotificationViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
