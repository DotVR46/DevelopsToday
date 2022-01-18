from django.urls import path

from comments.views import CommentListView, CommentCreateView, CommentUpdateView, CommentDeleteView, CommentDetailView

urlpatterns = [
    path('api/comments', CommentListView.as_view()),
    path('api/comments/create', CommentCreateView.as_view()),
    path('api/comments/update/<int:id>', CommentUpdateView.as_view()),
    path('api/comments/delete/<int:id>', CommentDeleteView.as_view()),
    path('api/comments/<int:id>', CommentDetailView.as_view()),
]