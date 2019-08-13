from django.db import models
from django.contrib.auth.models import User
from mdeditor.fields import MDTextField
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_count(self):
        return Post.objects.filter(category = self).count()

    def get_posts(self):
        return Post.objects.filter(category = self)

class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_count(self):
        return Post.objects.filter(tags = self).count()

    def get_posts(self):
        return Post.objects.filter(tags = self)


class Post(models.Model):
    title = models.CharField(max_length=200)
    # body = models.TextField()
    body = MDTextField()

    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    # excerpt = models.CharField(max_length=200, blank=True)

    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    tags = models.ManyToManyField(Tag, blank=True)

    author = models.ForeignKey(User, models.PROTECT)

    # click number
    clicks = models.IntegerField(default=0)

    def __str__(self):
        return self.title
