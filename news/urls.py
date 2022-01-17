from django.urls import path

from news.views import NewsListView, NewsDetailView

urlpatterns = [
    path('api/news', NewsListView.as_view()),
    path('api/news/<int:id>', NewsDetailView.as_view()),
]