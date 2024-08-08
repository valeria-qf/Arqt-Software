
from rest_framework import viewsets
from rest_framework.decorators import action
from core.models import Notification, NotificationTopic
from core.serializers import NotificationSerializer, TopicNotificationSerializer, UserSubscriptionSerializer
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import generics, permissions
from core.models import UserSubscription
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import AllowAny
from rest_framework.authentication import TokenAuthentication


class LoginView(APIView):
    permission_classes = [AllowAny]
    @csrf_exempt
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)

        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token':token.key})
        else:
            return Response({"error": "Invalid Credentials"}, status=status.HTTP_401_UNAUTHORIZED)

class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

    @action(detail=False, methods=['post'])
    def send(self, request):
        topic_name = request.data.get('topic')
        message = request.data.get('message')
        title = request.data.get('title')
        try:
            topic = NotificationTopic.objects.get(name=topic_name)
            notification = Notification.objects.create(topic=topic, title=title, message=message)

            channel_layer = get_channel_layer()
            topic_group_name = f"notifications_{topic_name}"

            async_to_sync(channel_layer.group_send)(
                topic_group_name,
                {
                    'type': 'notification_message',
                    'title': title,
                    'message': message,
                    'created_at': notification.created_at.isoformat()
                }
            )
            return Response({'status': 'notification sent'})
        except NotificationTopic.DoesNotExist:
            return Response({'status': 'topic does not exist'}, status=400)

class UserSubscriptionListView(generics.ListAPIView):
    serializer_class = UserSubscriptionSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get_queryset(self):
        return UserSubscription.objects.filter(user=self.request.user)
    
class TopicListView(viewsets.ReadOnlyModelViewSet):
    queryset = NotificationTopic.objects.all()
    serializer_class = TopicNotificationSerializer
    permission_classes = [AllowAny] 