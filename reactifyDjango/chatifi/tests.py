from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Tweet


# Create your tests here.

User = get_user_model()

class TweetTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='chatifi', password='11341134')

    def test_tweet_created(self):
        twt_obj = Tweet.objects.create(content = 'my tweet', user = self.user)
        self.assertEqual(twt_obj.id, 1)
        self.assertEqual(twt_obj.user, self.user)