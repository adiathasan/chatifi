from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('api/tweet/<str:pk>', tweet_detail, name='detail'),
    path('api/tweet/delete/<str:pk>', tweet_delete, name='deleteTweet'),
    path('api/tweets', all_tweets, name='tweets'),
    path('tweet/create', tweeting, name='tweetCreate'),
    path('tweet/action', tweet_action, name='tweetAction'),
]
