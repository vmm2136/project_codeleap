from django.db import models

class Career(models.Model):
    username = models.CharField(max_length=100, verbose_name='Username')
    title = models.TextField(null=False, blank=False, verbose_name='Title')
    content = models.TextField(null=False, blank=False, verbose_name='Content')
    created_dateTime = models.DateTimeField(auto_now=True, verbose_name='Created At')

    class Meta:
        ordering = ['username']
        verbose_name = ['Carrer']
