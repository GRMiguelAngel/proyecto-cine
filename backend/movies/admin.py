from django.contrib import admin

from .models import Movie, Genre

# Register your models here.

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['title', 'genre', 'duration']

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['name']
