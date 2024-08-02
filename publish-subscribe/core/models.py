from django.db import models

class User(models.Model):
    email = models.EmailField(unique=True)
class NotificationTopic(models.Model):
    name = models.CharField(max_length=255, unique=True)
class UserSubscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.ForeignKey(NotificationTopic, on_delete=models.CASCADE)

class Notification(models.Model):
    topic = models.ForeignKey(NotificationTopic, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
