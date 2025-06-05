from django.db import models
from django.contrib.auth.models import User

class Career(models.Model):
    username = models.CharField(max_length=100, verbose_name='Username')
    title = models.TextField(null=False, blank=False, verbose_name='Title')
    content = models.TextField(null=False, blank=False, verbose_name='Content')
    created_dateTime = models.DateTimeField(auto_now=True, verbose_name='Created At')

    class Meta:
        ordering = ['username']
        verbose_name = ['Carrer']

class Comment(models.Model):
    Career = models.ForeignKey(Career, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_dateTime = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_dateTime']
        verbose_name = ['Comment']
