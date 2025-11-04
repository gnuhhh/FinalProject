from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class ChatGroup(models.Model):
    group_name = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.group_name
    
class GroupMessage(models.Model):
    group = models.ForeignKey(ChatGroup, related_name='message', on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.sender.last_name}: {self.message}'
    
    class Meta:
        ordering = ['-created_at']