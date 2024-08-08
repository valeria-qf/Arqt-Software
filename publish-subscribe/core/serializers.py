from rest_framework import serializers
from .models import NotificationTopic, UserSubscription, Notification


class UserSubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSubscription
        fields = ['id', 'user', 'topic']

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['id', 'topic','title', 'message', 'created_at']


class TopicNotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificationTopic
        fields = ['id', 'name']