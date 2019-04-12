from django.contrib import admin
from .models import Post
from django.db import models
from pagedown.widgets import AdminPagedownWidget

@admin.register(Post)

class AlbumAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget(show_preview = True) },
    }


# Register your models here.
