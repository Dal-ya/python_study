from django.contrib import admin

# Register your models here.
from .models import Article, Comment, HashTag


@admin.register(Article, Comment, HashTag)
class FeedAdmin(admin.ModelAdmin):
    pass


# admin.site.register(Article)
# admin.site.register(Comment)
# admin.site.register(HashTag)