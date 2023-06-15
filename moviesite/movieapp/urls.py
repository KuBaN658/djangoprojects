from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_all_movies),
    path('movie/<slug:slug_movie>', views.show_one_movie, name='movie-detail'),
    path('directors', views.ListDirectors.as_view()),
    path('directors/<int:id_director>', views.show_one_director, name='director-detail'),
    path('actors', views.ListActors.as_view()),
    path('actors/<slug:slug_actor>', views.show_one_actor, name='actor-detail')
]
