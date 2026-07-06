from django.db import models
from django.conf import settings

class Message(models.Model):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='sent')
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='received')
    body = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['sent_at']

    def __str__(self):
        return f"{self.sender} -> {self.receiver}: '{self.body}'"