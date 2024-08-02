from django.db import models

class NotificationTopic(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name
class UserSubscription(models.Model):
    topic = models.ForeignKey(NotificationTopic, on_delete=models.CASCADE)
class Notification(models.Model):
    topic = models.ForeignKey(NotificationTopic, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
