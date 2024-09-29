from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='photos/categories')
    def __str__(self):
        return self.name


class Singer(models.Model):
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='photos/categories')

    def __str__(self):
        return self.name
class Song(models.Model):
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='photos/categories')
    audio = models.FileField(upload_to='audio')
    singer = models.ForeignKey(Singer, on_delete=models.CASCADE, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    def __str__(self):
        return self.name




class Album(models.Model):

    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='photos/categories')
    songs = models.ManyToManyField(Song)
    singers = models.ManyToManyField(Singer)
    def __str__(self):
        return self.name


class Playlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=255)
    songs = models.ManyToManyField(Song)
    def __str__(self):
        return self.name