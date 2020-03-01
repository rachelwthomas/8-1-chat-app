from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=255)
    avatar = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('accounts:profile_detail', args=(str(self.user.id)))
