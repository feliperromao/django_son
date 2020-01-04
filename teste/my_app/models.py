from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    description = models.CharField(max_length=255, verbose_name='Descrição')

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Categoria'
        # verbose_name_plural = 'Categorias' ## Django ja irá colocar o S no plural


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name='Título')
    subtitle = models.CharField(max_length=255, null=True, blank=True, verbose_name='Subtitulo')
    content = models.TextField(verbose_name='Conteúdo')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) # PROTECT, CASCADE, SET_NULL
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Artigo'
        verbose_name_plural = 'Artigos'