from django.contrib.auth.models import User
from django.db import models

from news.models import News


class Comment(models.Model):
    """
    Модель комментария
    """
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(News, on_delete=models.CASCADE)
    content = models.CharField(max_length=450)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.post.title} - {self.author.username}'

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
