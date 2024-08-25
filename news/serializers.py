from rest_framework.serializers import ModelSerializer
from .models import News, Comment

class NewsSerializer(ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'