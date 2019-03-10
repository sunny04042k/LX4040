from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify
from froala_editor.fields import FroalaField
class HTML(models.Model):
    likes = models.ManyToManyField(User, blank=True,related_name='html_likes')
    title = models.CharField(max_length=100)
    path = models.CharField(max_length=100,null=True)
    author = models.CharField(max_length=20,null=True)
    body  = FroalaField(null=True)
    date  = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True)

    def __str__(self):
        return self.title

    def total_likes(self):
        return self.likes.count()
    def get_absolute_url(self):
        return reverse("post_html",args=[self.path])
class CSS(models.Model):
    likes = models.ManyToManyField(User, blank=True,related_name='css_likes')
    title = models.CharField(max_length=100)
    path = models.CharField(max_length=100,null=True)
    author = models.CharField(max_length=20,null=True)
    body  = FroalaField(null=True)
    date  = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True)

    def __str__(self):
        return self.title

    def total_likes(self):
        return self.likes.count()

    #def get_absolute_url(self):
        #return reverse("post_html",args=[self.path])
class JS(models.Model):
    likes = models.ManyToManyField(User, blank=True,related_name='js_likes')
    title = models.CharField(max_length=100)
    path = models.CharField(max_length=100,null=True)
    author = models.CharField(max_length=20,null=True)
    body  = FroalaField(null=True)
    date  = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True)

    def __str__(self):
        return self.title

    def total_likes(self):
        return self.likes.count()

    #def get_absolute_url(self):
        #return reverse("post_html",args=[self.path])
