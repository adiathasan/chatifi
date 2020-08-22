from django.http import JsonResponse
from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Tweet
import random

# Create your views here.


def home(request):
    tweets = Tweet.objects.all()
    json_res = [{'id': obj.id, 'content': obj.content, 'likes': random.randint(0, 122)} for obj in tweets]
    return render(request, 'chatifi/index.html', {})


# rest api views>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


def all_tweets(request):
    tweets = Tweet.objects.all()
    json_res = [{'id': obj.id, 'content': obj.content, 'likes': random.randint(0, 123)} for obj in tweets]
    data = {
        'response': json_res
    }
    return JsonResponse(data)


def tweet_detail(request, pk):
    tweet = get_object_or_404(Tweet, id=pk)
    obj = {
        'id': pk,
        'content': tweet.content,
        # 'img': tweet.img.url
    }
    return JsonResponse(obj)
