from django import forms
from .models import Tweet

lengthTweet = 200

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['content']


    def clean_content(self):
       content = self.cleaned_data.get('content')
       if len(content) > lengthTweet:
           raise forms.ValidationError('This tweet is too long')
       return content