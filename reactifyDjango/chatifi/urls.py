from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('api/tweet/<str:pk>', tweet_detail, name='detail'),
    path('api/tweets', all_tweets, name='home'),
]
