from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
import json
from core.models import NotificationTopic, UserSubscription
from django.contrib.auth.models import AnonymousUser
from rest_framework.authtoken.models import Token
from urllib.parse import parse_qs

class NotificationConsumer(WebsocketConsumer):
    def connect(self):
        token = self.get_token_from_query(self.scope['query_string'].decode())
        user = self.authenticate_token(token)
        
        if not user or not user.is_authenticated:
            self.close()
            return

        self.user = user

        # Resubscreve o usuário nos tópicos existentes
        self.resubscribe_to_topics()

        self.accept()

        self.send(text_data=json.dumps({
            'type': 'connection',
            'message': 'Connected successfully',
            'user': self.user.username
        }))

    def disconnect(self, close_code):
        # Lógica de desconexão pode ser removida ou adaptada conforme necessário
        pass

    def receive(self, text_data):
        if not self.user.is_authenticated:
            self.send(text_data=json.dumps({
                'type': 'error',
                'message': 'User not authenticated'
            }))
            return 
        
        data = json.loads(text_data)
        message_type = data.get('type')
        topic_name = data.get('topic')

        if message_type == 'subscribe' and topic_name:
            self.subscribe_to_topic(topic_name)
        elif message_type == 'unsubscribe' and topic_name:
            self.unsubscribe_from_topic(topic_name)
        else:
            self.send(text_data=json.dumps({
                'type': 'error',
                'message': 'Invalid message or missing topic'
            }))

    def subscribe_to_topic(self, topic_name):
        topic_group_name = f"notifications_{topic_name}"
        
        try:
            topic = NotificationTopic.objects.get(name=topic_name)
        except NotificationTopic.DoesNotExist:
            self.send(text_data=json.dumps({
                'type': 'subscription_error',
                'message': 'Topic does not exist'
            }))
            return

        # Save subscription to database
        UserSubscription.objects.get_or_create(user=self.user, topic=topic)
        async_to_sync(self.channel_layer.group_add)(
            topic_group_name,
            self.channel_name
        )
        self.send(text_data=json.dumps({
            'type': 'subscription_success',
            'message': f'Subscribed to {topic_name}'
        }))

    def unsubscribe_from_topic(self, topic_name):
        topic_group_name = f"notifications_{topic_name}"
        
        try:
            topic = NotificationTopic.objects.get(name=topic_name)
        except NotificationTopic.DoesNotExist:
            self.send(text_data=json.dumps({
                'type': 'unsubscription_error',
                'message': 'Topic does not exist'
            }))
            return

        # Remove subscription from database
        UserSubscription.objects.filter(user=self.user, topic=topic).delete()
        async_to_sync(self.channel_layer.group_discard)(
            topic_group_name,
            self.channel_name
        )
        self.send(text_data=json.dumps({
            'type': 'unsubscription_success',
            'message': f'Unsubscribed from {topic_name}'
        }))

    def notification_message(self, event):
        title = event['title']
        message = event['message']
        created_at = event['created_at']
        self.send(text_data=json.dumps({
            'title': title,
            'message': message,
            'created_at': created_at  
        }))

    def resubscribe_to_topics(self):
        subscriptions = UserSubscription.objects.filter(user=self.user)
        for subscription in subscriptions:
            topic_name = subscription.topic.name
            topic_group_name = f"notifications_{topic_name}"
            async_to_sync(self.channel_layer.group_add)(
                topic_group_name,
                self.channel_name
            )
            self.send(text_data=json.dumps({
                'type': 'subscription_success',
                'message': f'Resubscribed to {topic_name}'
            }))

    def get_token_from_query(self, query_string):
        query_params = parse_qs(query_string)
        return query_params.get('token', [None])[0]

    def authenticate_token(self, token):       
        try:
            token_obj = Token.objects.get(key=token)
            return token_obj.user
        except Token.DoesNotExist:
            return AnonymousUser()
