from django.http import JsonResponse
from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
from .models import Tweet
from .forms import TweetForm
from django.utils.http import is_safe_url
# from .serializers import tweetPostSerializer

# Create your views here.


def home(request):
    tweets = Tweet.objects.all().order_by('-id')
    return render(request, 'chatifi/index.html', {})


def tweeting(request):
    form = TweetForm(request.POST or None)
    next_url = request.POST.get('next') or None
    if form.is_valid():
        f = form.save(commit=False)
        f.save()
        if next_url is not None and is_safe_url(next_url, allowed_hosts=['*']):
            return redirect(next_url)
        form = TweetForm()
    context = {'form': form}
    return render(request, 'chatifi/tweetForm.html', context)


# rest api views>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


def all_tweets(request):
    tweets = Tweet.objects.all()
    json_res = [obj.serializer() for obj in tweets]
    data = {
        'response': json_res
    }
    return JsonResponse(data)


def tweet_detail(request, pk):
    tweet = get_object_or_404(Tweet, id=pk)
    obj = tweet.serializer()
    return JsonResponse(obj)

#
# @api_view(['GET', 'POST'])
# def tweet_list(request):
#     """
#     List all code snippets, or create a new snippet.
#     """
#     if request.method == 'GET':
#         tweets = Tweet.objects.all().order_by('-id')
#         serializer = tweetPostSerializer(tweets, many=True)
#         return Response(serializer.data)
#
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = tweetPostSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)
#
#
# @csrf_exempt
# def snippet_detail(request, pk):
#     """
#     Retrieve, update or delete a code snippet.
#     """
#     try:
#         snippet = Snippet.objects.get(pk=pk)
#     except Snippet.DoesNotExist:
#         return HttpResponse(status=404)
#
#     if request.method == 'GET':
#         serializer = SnippetSerializer(snippet)
#         return JsonResponse(serializer.data)
#
#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = SnippetSerializer(snippet, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)
#
#     elif request.method == 'DELETE':
#         snippet.delete()

#         return HttpResponse(status=204)
