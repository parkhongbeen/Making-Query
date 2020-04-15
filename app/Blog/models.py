from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    is_published = models.BooleanField(default=False)


class Item(models.Model):
    post = models.CharField(Post, max_length=20)
