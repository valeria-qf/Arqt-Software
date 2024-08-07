from django.urls import path, include
from rest_framework import routers
from core.views import LoginView, NotificationViewSet

router = routers.DefaultRouter()

router.register(r'notifications', NotificationViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('login/', LoginView.as_view(), name='login'),
]
