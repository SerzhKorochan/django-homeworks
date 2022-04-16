from pyexpat import model
from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_at']


class Scope(models.Model):
    name = models.CharField(max_length=40, verbose_name='Разделы')
    articles = models.ManyToManyField(Article, through='ArticleScope')

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'


class ArticleScope(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name = 'Статья', related_name='scopes')
    tag = models.ForeignKey(Scope, on_delete=models.CASCADE, verbose_name = 'Раздел')
    is_main = models.BooleanField(verbose_name='Основной')

    class Meta:
        verbose_name = 'Тематики статьи'
        verbose_name_plural = 'Тематики статей'
        ordering = ['-is_main']
