from rest_framework import serializers
from .models import NotificationTopic, UserSubscription, Notification


class UserSubscriptionSerializer(serializers.ModelSerializer):
    topic_name = serializers.SerializerMethodField()
    class Meta:
        model = UserSubscription
        fields = ['id', 'user', 'topic_name']

    def get_topic_name(self, obj):
        return obj.topic.name if obj.topic else None
class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['id', 'topic','title', 'message', 'created_at']


class TopicNotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificationTopic
        fields = ['id', 'name']