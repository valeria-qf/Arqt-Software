from rest_framework import serializers
from .models import UserSubscription, Notification


# core/serializers.py

class UserSubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSubscription
        fields = ['user', 'topic']
        
    def validate(self, data):
        user = data.get('user')
        topic = data.get('topic')
        if UserSubscription.objects.filter(user=user, topic=topic).exists():
            raise serializers.ValidationError('User is already subscribed to this topic.')
        return data
