from rest_framework import serializers
from .models import Tweet

lengthTweet = 200

class tweetPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = ['content', 'user']


    def validate_content(self, value):
        if len(value) > lengthTweet:
            raise value.ValidationError('This tweet is too long')
        return value

