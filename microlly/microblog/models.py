from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class BlogPost(models.Model):
    title = models.CharField(max_length=32)
    body = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    postdate = models.DateTimeField(auto_now_add=True)
    editdate = models.DateTimeField(auto_now=True)    
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
    def  __str__(self):
        return self.title