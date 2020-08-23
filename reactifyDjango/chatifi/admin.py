from django.contrib import admin
from .models import *


# Register your models here.


class TweetLikeAdmin(admin.TabularInline):
    model = TweetLike


class TweetAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'user']
    search_fields = ['content', 'user__username', 'user__email']
    inlines = [TweetLikeAdmin]
    class Meta:
        model = Tweet

admin.site.register(Tweet, TweetAdmin)
admin.site.register(TweetLike)

