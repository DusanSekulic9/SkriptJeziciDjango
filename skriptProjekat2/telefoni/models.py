from django.db import models
from django.contrib.auth.models import Userg
# Create your models here.
class Article(models.Model):
    marka = models.CharField(max_length=32,default='')
    naziv = models.CharField(max_length=32,default='')
    sistem = models.CharField(max_length=32, default='')
    num_views = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.marka + ' ' + self.naziv


class Comment(models.Model):
    content = models.CharField(max_length=64)
    num_views = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.content