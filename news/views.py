from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from rest_framework.generics import ListAPIView, RetrieveAPIView, DestroyAPIView, CreateAPIView, UpdateAPIView
from rest_framework.pagination import PageNumberPagination

from news.models import News
from news.permissions import IsOwnerOrReadOnly
from news.serializers import NewsListSerializer, NewsDetailSerializer


class CustomPagination(PageNumberPagination):
    """
    Пагинация для списка новостей и списка комментариев
    """
    page_size = 10
    page_query_param = 'p'


class NewsListView(ListAPIView):
    """
    Список всех новостей с пагинацией
    """
    queryset = News.objects.all()
    serializer_class = NewsListSerializer
    pagination_class = CustomPagination


class NewsDetailView(RetrieveAPIView):
    """
    Детальный просмотр новости по id
    """
    queryset = News.objects.all()
    serializer_class = NewsDetailSerializer
    lookup_field = 'id'


class NewsDeleteView(DestroyAPIView):
    """
    Удаление новости по id. Удалять может только owner
    """
    queryset = News.objects.all()
    serializer_class = NewsDetailSerializer
    permission_classes = [IsOwnerOrReadOnly]
    lookup_field = 'id'


class NewsUpdateView(UpdateAPIView):
    """
    Изменение новости по id. Изменять может только owner
    """
    queryset = News.objects.all()
    serializer_class = NewsDetailSerializer
    permission_classes = [IsOwnerOrReadOnly]
    lookup_field = 'id'


class NewsCreateView(CreateAPIView):
    """
    Создание объекта новости. Нужно указать автора
    """
    queryset = News.objects.all()
    serializer_class = NewsDetailSerializer


def vote_news(request, id):
    """
    Эндпоинт для голосования
    :param request:
    :param id:
    :return:
    """
    news = get_object_or_404(News, id=id)
    news.upvotes += 1
    news.save()
    return HttpResponse('ok')
