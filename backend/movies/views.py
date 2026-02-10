from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, JsonResponse, HttpResponseNotAllowed
from .serializers import MovieSerializer
from .models import Movie
from datetime import time

# Create your views here.

def movie_list(request: HttpRequest) -> HttpResponse:
    movies = Movie.objects.all()
    serialized = MovieSerializer(movies)
    
    return JsonResponse({'movies': serialized.serialize()})

def movie_detail(request: HttpRequest, title: str) -> HttpResponse:
    movie = Movie.objects.get(title=title)
    serialized = MovieSerializer(movie)

    return JsonResponse({'movie': serialized.serialize()})

def add_movie(request: HttpRequest, title: str, duration: time) -> HttpResponse:
    if request.method == 'POST':
        new_movie = Movie.objects.create(title=title, duration=duration)
        return HttpResponse(f'created new movie: {new_movie}')
    return HttpResponseNotAllowed(f'Method {request.method} not allow')
    
