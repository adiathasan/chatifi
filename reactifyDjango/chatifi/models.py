from django.db import models
import random
# Create your models here.


class Tweet(models.Model):
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
