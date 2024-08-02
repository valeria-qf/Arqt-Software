# core/consumers.py
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
import json
from core.models import NotificationTopic, UserSubscription

class NotificationConsumer(WebsocketConsumer):
    def connect(self):
        # Get topic from URL route kwargs
        self.topic = self.scope['url_route']['kwargs'].get('topic', 'default_topic')
        self.topic_group_name = f"notifications_{self.topic.replace('@', '_').replace('.', '_')}"
        # Add WebSocket channel to group
        async_to_sync(self.channel_layer.group_add)(
            self.topic_group_name,
            self.channel_name
        )
        self.accept()

    def disconnect(self, close_code):
        # Remove WebSocket channel from group
        async_to_sync(self.channel_layer.group_discard)(
            self.topic_group_name,
            self.channel_name
        )

    def receive(self, text_data):
        data = json.loads(text_data)
        if data.get('type') == 'subscribe':
            self.subscribe_to_topic(data.get('topic'))
        elif data.get('type') == 'unsubscribe':
            self.unsubscribe_from_topic(data.get('topic'))

    def subscribe_to_topic(self, topic_name):
        topic_name = topic_name.replace('@', '_').replace('.', '_')
        self.topic_group_name = f"notifications_{topic_name}"
        
        # Get or create topic
        try:
            topic = NotificationTopic.objects.get(name=topic_name)
        except NotificationTopic.DoesNotExist:
            self.send(text_data=json.dumps({
                'type': 'subscription_error',
                'message': 'Topic does not exist'
            }))
            return

        # Save subscription to database
        UserSubscription.objects.get_or_create(topic=topic)
        async_to_sync(self.channel_layer.group_add)(
            self.topic_group_name,
            self.channel_name
        )
        self.send(text_data=json.dumps({
            'type': 'subscription_success',
            'message': f'Subscribed to {topic_name}'
        }))

    def unsubscribe_from_topic(self, topic_name):
        topic_name = topic_name.replace('@', '_').replace('.', '_')
        self.topic_group_name = f"notifications_{topic_name}"
        
        # Get or create topic
        try:
            topic = NotificationTopic.objects.get(name=topic_name)
        except NotificationTopic.DoesNotExist:
            self.send(text_data=json.dumps({
                'type': 'unsubscription_error',
                'message': 'Topic does not exist'
            }))
            return

        # Remove subscription from database
        UserSubscription.objects.filter(topic=topic).delete()
        async_to_sync(self.channel_layer.group_discard)(
            self.topic_group_name,
            self.channel_name
        )
        self.send(text_data=json.dumps({
            'type': 'unsubscription_success',
            'message': f'Unsubscribed from {topic_name}'
        }))

    def notification_message(self, event):
        message = event['message']
        self.send(text_data=json.dumps({
            'type': 'notification',
            'message': message
        }))
