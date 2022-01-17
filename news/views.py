from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
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
