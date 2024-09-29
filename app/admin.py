from django.contrib import admin

from app.models import Category, Singer, Song, Album, Playlist

# Register your models here.


admin.site.register([Category,Singer,Song,Album,Playlist])