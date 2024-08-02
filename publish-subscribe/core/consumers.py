from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth.models import User
from .models import UserSubscription

class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user = self.scope["user"]
        if not self.user.is_authenticated:
            await self.close()
            return

        self.topic_name = self.scope['url_route']['kwargs'].get('topic_name')
        self.room_group_name = f'notifications_{self.topic_name}'

        if not UserSubscription.objects.filter(user=self.user, topic__name=self.topic_name).exists():
            topic = await self.get_topic()
            UserSubscription.objects.create(user=self.user, topic=topic)

        await self.channel_layer.group_add(
            self.room_group_name,
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

    async def receive(self, text_data):
        # This method can be used if you want to handle incoming WebSocket messages
        pass

    async def send_notification(self, event):
        message = event['message']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))

    async def get_topic(self):
        from .models import Topic
        return await Topic.objects.get(name=self.topic_name)
