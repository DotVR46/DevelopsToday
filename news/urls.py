from django.urls import path

from news.views import NewsListView, NewsDetailView, vote_news, NewsDeleteView, NewsCreateView, NewsUpdateView

urlpatterns = [
    path('api/news', NewsListView.as_view()),
    path('api/news/create', NewsCreateView.as_view()),
    path('api/news/<int:id>', NewsDetailView.as_view()),
    path('api/news/update/<int:id>', NewsUpdateView.as_view()),
    path('api/news/delete/<int:id>', NewsDeleteView.as_view()),
    path('api/news/vote/<int:id>', vote_news)
]