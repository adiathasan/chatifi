from django.http import JsonResponse
from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Tweet
from .forms import TweetForm
from django.utils.http import is_safe_url
from django.conf import settings
from .serializers import TweetPostSerializer, TweetActionSerializer, TweetGetSerializer


# Create your views here.


def home(request):
    return render(request, 'chatifi/index.html', {})


# rest api framework views>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

@api_view(['GET'])
def all_tweets(request):
    tweets = Tweet.objects.all().order_by('-id')
    serialize = TweetGetSerializer(tweets, many=True)
    return Response(serialize.data)


@api_view(['GET'])
def tweet_detail(request, pk):
    tweet = get_object_or_404(Tweet, id=pk)
    serializer = TweetGetSerializer(tweet, many=False)
    return Response(serializer.data)


@permission_classes([IsAuthenticated])
@api_view(['POST'])
def tweeting(request):
    serialize = TweetPostSerializer(data=request.data)
    if serialize.is_valid(raise_exception=True):
        serialize.save(user=request.user)
        return Response(serialize.data, status=201)
    return JsonResponse(serialize.errors, status=401)


@api_view(['DELETE', 'POST'])
@permission_classes([IsAuthenticated])
def tweet_delete(request, pk):
    tweet = get_object_or_404(Tweet, id=pk)
    person = Tweet.objects.filter(user=request.user)
    if not person.exists():
        return Response({'message': 'You are not authorized to delete this post'})
    tweet.delete()
    return Response('Tweet deleted successfully')


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def tweet_action(request):
    serializer = TweetActionSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        data = serializer.validated_data
        tweet_id = data.get('id')
        action = data.get('action')
    person = Tweet.objects.filter(id=tweet_id)
    if not person.exists():
        return Response({}, status=404)
    obj = person.first()
    serializer = TweetGetSerializer(obj)
    # if person is None:
    #     return Response({'message': 'User does not exits'}, status=404)
    if action == 'like':
        obj.like.add(request.user)
        return Response(serializer.data, status=200)
    elif action == 'unlike':
        obj.like.remove(request.user)
        return Response(serializer.data, status=200)
    elif action == 'retweet':
        parent_obj = obj
        new_tweet = Tweet.objects.create(user=request.user,
                                         Parent=parent_obj)
        serializer = TweetGetSerializer(new_tweet)
        return Response(serializer.data, status=201)
    return Response({}, status=200)

# >>>>>>>>>>>>>>>>>>>>>>>> Old pure django api views


# pure django views....>>>>>>>>>>>>>>>>>>>>>>>>
# def tweeting(request):
#     user = request.user
#     if not request.user.is_authenticated:
#         user = None
#         if request.is_ajax():
#             return JsonResponse({}, status=401)
#         return redirect(settings.LOGIN_URL)
#     form = TweetForm(request.POST or None)
#     next_url = request.POST.get('next') or None
#
#     if form.is_valid():
#         f = form.save(commit=False)
#         f.user = user
#         f.save()
#         if request.is_ajax():
#             return JsonResponse(f.serializer(), status=201)
#         if next_url is not None and is_safe_url(next_url, allowed_hosts=['*']):
#             return redirect(next_url)
#         form = TweetForm()
#
#     if form.errors:
#         if request.is_ajax():
#             return JsonResponse(form.errors, status=400)
#
#     context = {'form': form}
#     return render(request, 'chatifi/tweetForm.html', context)

# def all_tweets(request):
#     tweets = Tweet.objects.all().order_by('-id')
#     json_res = [obj.serializer() for obj in tweets]
#     data = {
#         'response': json_res
#     }
#     return JsonResponse(data)


# def tweet_detail(request, pk):
#     tweet = get_object_or_404(Tweet, id=pk)
#     obj = tweet.serializer()
#     return JsonResponse(obj)
