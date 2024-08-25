from django.contrib import admin
from .models import News, Comment

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')
    search_fields = ('title', 'text', 'author__name')
    list_filter = ['author']
    filter_horizontal = ('views',)
    list_per_page = 25

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('news_comment', 'author')
    search_fields = ('text', 'author__username', 'news_comment__title')
    list_filter = ['author']
    list_per_page = 25
