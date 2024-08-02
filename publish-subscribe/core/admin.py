from django.contrib import admin
from .models import NotificationTopic, UserSubscription, Notification

@admin.register(NotificationTopic)
class NotificationTopicAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(UserSubscription)
class UserSubscriptionAdmin(admin.ModelAdmin):
    list_display = ('topic',)

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('topic', 'message', 'created_at')
