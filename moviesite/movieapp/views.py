from django.shortcuts import render, get_object_or_404
from .models import Movie

def show_all_movies(request):
    movies = Movie.objects.all()
    # for movie in movies:
    #     movie.save()
    return render(request, 'movieapp/all_movies.html', {
        'movies': movies,
    })


def show_one_movie(request, slug_movie: str):
    movie = get_object_or_404(Movie, slug=slug_movie)
    return render(request, 'movieapp/one_movie.html', {
        'movie': movie,
    })