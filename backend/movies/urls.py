from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = (
    path('', views.movie_list, name='movie-list'),
    path('add/', views.add_movie, name='add-movie'),
    path('<str:title>/', views.movie_detail, name='movie-detail'),
)