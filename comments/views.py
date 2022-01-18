from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, RetrieveAPIView, UpdateAPIView

from comments.models import Comment
from comments.serializers import CommentSerializer
from news.permissions import IsOwnerOrReadOnly
from news.views import CustomPagination


class CommentListView(ListAPIView):
    """
    Список комментариев
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    pagination_class = CustomPagination


class CommentCreateView(CreateAPIView):
    """
    Создание комментария. Нужно указать пост,
    которому он принадледит и автора.
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentDeleteView(DestroyAPIView):
    """
    Удаление комментария. Удалить может только owner
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsOwnerOrReadOnly]
    lookup_field = 'id'


class CommentDetailView(RetrieveAPIView):
    """
    Детальный просмотр комментария по id
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field = 'id'


class CommentUpdateView(UpdateAPIView):
    """
    Изменение комментария. Изменить может только owner
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsOwnerOrReadOnly]
    lookup_field = 'id'
