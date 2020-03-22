from django.contrib import admin
from .models import Profile, Post

# Register your models here.

admin.site.register(Profile)
admin.site.register(Post)
"""
@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'image', 'created']
    list_filter = ['created']
"""