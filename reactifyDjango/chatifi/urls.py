from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('tweet/create', tweeting, name='tweetCreate'),
    path('api/tweets', all_tweets, name='tweets'),
    path('api/tweet/<str:pk>', tweet_detail, name='detail'),
    path('api/tweet/delete/<str:pk>', tweet_delete, name='deleteTweet'),
    path('api/tweets/action', tweet_action, name='tweetAction'),
]
