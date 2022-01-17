from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from comments.serializers import CommentSerializer
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
    author = serializers.CharField(source='author.username', read_only=True)
    author_id = serializers.IntegerField(source='author.id', write_only=True)
    comments = CommentSerializer(many=True, source='commented_post', read_only=True)

    class Meta:
        model = News
        fields = ('id', 'title', 'link', 'article', 'author', 'author_id', 'created', 'upvotes', 'comments')

    def create(self, validated_data):
        print(validated_data)
        user_id = validated_data.pop('author')['id']
        user = User.objects.get(id=user_id)
        news = News.objects.create(author=user, **validated_data)
        news.save()
        return news

    def update(self, instance, validated_data):
        instance.__dict__.update(validated_data)
        instance.save()
        return instance

