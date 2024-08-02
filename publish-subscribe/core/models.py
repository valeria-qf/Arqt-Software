# models.py
from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
class Topic(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class UserSubscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} subscribed to {self.topic}"

class Notification(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification for {self.topic} at {self.timestamp}"
