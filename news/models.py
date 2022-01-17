from django.contrib.auth.models import User
from django.db import models


class News(models.Model):
    """
    Модель новостей
    """
    title = models.CharField(max_length=100)
    article = models.TextField(blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    created = models.DateTimeField(auto_now_add=True)
    upvotes = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.title} - {self.author.username}'

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created']
