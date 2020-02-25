from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

User = get_user_model()
# Create your models here.

class Room(models.Model):
    name = models.CharField(max_length=255)
    messages = models.ManyToManyField('Message', related_name='chat_rooms')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('chat_app:chat_rooms')


class Message(models.Model):
    message = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.message
