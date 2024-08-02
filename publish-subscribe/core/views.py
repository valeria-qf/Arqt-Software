
from rest_framework import viewsets
from rest_framework.decorators import action
from core.models import Notification, NotificationTopic
from core.serializers import NotificationSerializer
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from rest_framework.response import Response

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

            channel_layer = get_channel_layer()
            sanitized_topic_name = topic_name.replace('@', '_').replace('.', '_')
            topic_group_name = f"notifications_{sanitized_topic_name}"

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
