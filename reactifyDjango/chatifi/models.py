from django.db import models

# Create your models here.


class Tweet(models.Model):
    content = models.TextField(blank=True, null=True)
    img = models.FileField(blank=True, null=True, upload_to='images/')

    def __str__(self):
        return self.content