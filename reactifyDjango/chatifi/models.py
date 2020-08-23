from django.db import models
import random
from django.conf import settings

# Create your models here.

User = settings.AUTH_USER_MODEL


class TweetLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tweet = models.ForeignKey("Tweet", on_delete=models.CASCADE)
    Time = models.DateTimeField(auto_now_add=True)


class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    like = models.ManyToManyField(User, blank=True, related_name='tweet_user', through="TweetLike")
    content = models.TextField(blank=True, null=True)
    img = models.FileField(blank=True, null=True, upload_to='images/')
    Parent = models.ForeignKey("self", null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.content

    @property
    def is_retweet(self):
        return self.Parent != None
