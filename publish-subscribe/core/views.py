
from rest_framework import viewsets
from rest_framework.decorators import action
from core.models import Notification, NotificationTopic, User, UserSubscription
from core.serializers import NotificationSerializer, UserSubscriptionSerializer
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from rest_framework.response import Response
from rest_framework.exceptions import NotFound

class UserSubscriptionViewSet(viewsets.ModelViewSet):
    queryset = UserSubscription.objects.all()
    serializer_class = UserSubscriptionSerializer

    @action(detail=True, methods=['post'])
    def subscribe(self, request, pk=None):
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise NotFound('User not found')

        topic_name = request.data.get('topic')
        try:
            topic = NotificationTopic.objects.get(name=topic_name)
            UserSubscription.objects.get_or_create(user=user, topic=topic)
            return Response({'status': 'subscribed'})
        except NotificationTopic.DoesNotExist:
            return Response({'status': 'topic does not exist'}, status=400)

class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

    @action(detail=False, methods=['post'])
    def send(self, request):
        topic_name = request.data.get('topic')
        message = request.data.get('message')
        try:
            topic = NotificationTopic.objects.get(name=topic_name)
            Notification.objects.create(topic=topic, message=message)

            # Prepare the channel layer
            channel_layer = get_channel_layer()
            sanitized_topic_name = topic_name.replace('@', '_').replace('.', '_')
            topic_group_name = f"notifications_{sanitized_topic_name}"

            # Send notification to the group
            async_to_sync(channel_layer.group_send)(
                topic_group_name,
                {
                    'type': 'notification_message',
                    'message': message
                }
            )

            return Response({'status': 'notification sent'})
        except NotificationTopic.DoesNotExist:
            return Response({'status': 'topic does not exist'}, status=400)
