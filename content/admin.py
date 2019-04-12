from django.contrib import admin
from .models import Album, Photo, Video
from django.db import models

admin.site.register(Album)
admin.site.register(Photo)
admin.site.register(Video)


# Register your models here.
