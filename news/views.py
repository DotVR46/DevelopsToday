from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from rest_framework.generics import ListAPIView, RetrieveAPIView, DestroyAPIView, CreateAPIView, UpdateAPIView
from rest_framework.pagination import PageNumberPagination

from news.models import News
from news.serializers import NewsListSerializer, NewsDetailSerializer


class CustomPagination(PageNumberPagination):
    page_size = 10
    page_query_param = 'p'


class NewsListView(ListAPIView):
    serializer_class = NewsListSerializer
    pagination_class = CustomPagination
    queryset = News.objects.all()


class NewsDetailView(RetrieveAPIView):
    serializer_class = NewsDetailSerializer
    lookup_field = 'id'
    queryset = News.objects.all()


class NewsDeleteView(DestroyAPIView):
    serializer_class = NewsDetailSerializer
    lookup_field = 'id'
    queryset = News.objects.all()


class NewsUpdateView(UpdateAPIView):
    serializer_class = NewsDetailSerializer
    lookup_field = 'id'
    queryset = News.objects.all()


class NewsCreateView(CreateAPIView):
    serializer_class = NewsDetailSerializer
    queryset = News.objects.all()


def vote_news(request, id):
    news = get_object_or_404(News, id=id)
    news.upvotes += 1
    news.save()
    return HttpResponse('ok')
