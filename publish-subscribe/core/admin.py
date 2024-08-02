from django.contrib import admin
from .models import Topic, UserSubscription, Notification


@admin.register(Topic)
class NotificationTopicAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(UserSubscription)
class UserSubscriptionAdmin(admin.ModelAdmin):
    list_display = ('user', 'topic')

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('topic', 'message', 'created_at')
