from django.shortcuts import render
from rest_framework import viewsets
from .models import News, Comment
from .serializers import NewsSerializer, CommentSerializer

class NewsView(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

class CommentView(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer