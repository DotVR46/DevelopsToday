from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from news.models import News


class NewsListSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    author = serializers.CharField(source='author.username')
    created = serializers.DateTimeField()
    upvotes = serializers.IntegerField()
    comments_count = SerializerMethodField()

    def get_comments_count(self, obj):
        total = obj.commented_post.count()
        return total


class NewsDetailSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='author.username')
    class Meta:
        model = News
        fields = ('id', 'title', 'link', 'article', 'author', 'created', 'upvotes')
