from rest_framework import serializers
from .models import Tweet
from django.conf import settings

LENGTH_OF_TWEET = settings.LENGTH_OF_TWEET
TWEET_ACTION_OPTIONS = settings.TWEET_ACTION_OPTIONS

class TweetPostSerializer(serializers.ModelSerializer):
    like = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Tweet
        fields = ['content','id', 'like' ]

    def get_like(self, likes):
        return likes.like.count()

    def validate_content(self, value):
        if len(value) > settings.LENGTH_OF_TWEET:
            raise serializers.ValidationError('This tweet is too long')
        return value


class TweetGetSerializer(serializers.ModelSerializer):
    like = serializers.SerializerMethodField(read_only=True)
    Parent = TweetPostSerializer(read_only=True)

    class Meta:
        model = Tweet
        fields = ['content','id', 'like', 'Parent', 'is_retweet']

    def get_like(self, likes):
        return likes.like.count()


class TweetActionSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    action = serializers.CharField()

    def validate_action(self, value):
        value = value.lower().strip() # ' AbC ' -> 'abc'
        if not value in TWEET_ACTION_OPTIONS:
            raise serializers.ValidationError('Not a valid action')
        return value

