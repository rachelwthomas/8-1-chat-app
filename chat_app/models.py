from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

User = get_user_model()
# Create your models here.

class Room(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='rooms')
    members = models.ManyToManyField(User)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('chat_app:chat_rooms')


class Message(models.Model):
    text = models.CharField(max_length=255, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.text[:50]

    def get_absolute_url(self):
        return reverse('chat_app:chat_detail', args=(self.room_id,))     
