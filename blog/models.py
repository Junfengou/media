from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.utils import timezone
from django.urls import reverse


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pic')
    my_story = models.CharField(max_length=200, null=True)

    def __str__(self):
        return f'{self.user.username} Profile'


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    caption = models.TextField()
    img = models.ImageField(default=True, null=True)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.caption

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
