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
        action_type = data.get('type')

        if action_type == 'subscribe':
            topic_name = data.get('topic')
            if topic_name:
                self.subscribe_to_topic(topic_name)
        elif action_type == 'notification':
            topic_name = data.get('topic')
            message = data.get('message')
            if topic_name and message:
                self.send_notification(topic_name, message)

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
