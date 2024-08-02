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

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
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
