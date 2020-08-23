from django.db import models
import random
from django.conf import settings
# Create your models here.

User = settings.AUTH_USER_MODEL


class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    content = models.TextField(blank=True, null=True)
    img = models.FileField(blank=True, null=True, upload_to='images/')

    def __str__(self):
        return self.content

    def serializer(self):
        return {
            'id': self.id,
            'content': self.content,
            # 'img': self.img,
            'likes': random.randint(0, 122)
        }
