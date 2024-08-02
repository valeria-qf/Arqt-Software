# core/consumers.py
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
import json

class NotificationConsumer(WebsocketConsumer):
    def connect(self):
        self.topic = self.scope['url_route']['kwargs'].get('topic', 'default_topic')
        self.channel_layer.group_add(
            self.topic,
            self.channel_name
        )
        self.accept()

    def disconnect(self, close_code):
        self.channel_layer.group_discard(
            self.topic,
            self.channel_name
        )

    def receive(self, text_data):
        data = json.loads(text_data)
        if data.get('type') == 'subscribe':
            self.subscribe_to_topic(data.get('topic'))
        elif data.get('type') == 'notification':
            self.send_notification(data.get('topic'), data.get('message'))

    def subscribe_to_topic(self, topic_name):
        self.topic = f"notifications_{topic_name}"
        self.channel_layer.group_add(
            self.topic,
            self.channel_name
        )
        self.send(text_data=json.dumps({
            'type': 'subscription_success',
            'message': f'Subscribed to {topic_name}'
        }))

    def send_notification(self, topic_name, message):
        self.topic = f"notifications_{topic_name}"
        async_to_sync(self.channel_layer.group_send)(
            self.topic,
            {
                'type': 'notification_message',
                'message': message
            }
        )

    def notification_message(self, event):
        message = event['message']
        self.send(text_data=json.dumps({
            'type': 'notification',
            'message': message
        }))
