from django.shortcuts import render, get_object_or_404
from .models import Movie, Director
from django.db.models import F, Avg, Min, Max



def show_all_movies(request):
    movies = Movie.objects.order_by(F('rating').desc(nulls_last=True))
    total = movies.count()
    agg = movies.aggregate(Avg('budget'), Min('rating'), Max('rating'))
    # for movie in movies:
    #     movie.save()
    return render(request, 'movieapp/all_movies.html', {
        'movies': movies,
        'agg': agg,
        'total': total
    })


def show_one_movie(request, slug_movie: str):
    movie = get_object_or_404(Movie, slug=slug_movie)
    return render(request, 'movieapp/one_movie.html', {
        'movie': movie,
    })


def show_all_directors(request):
    directors = Director.objects.order_by(F('first_name').asc(nulls_last=True))
    total = directors.count()
    return render(request, 'movieapp/all_directors.html', {
        'directors': directors,
        'total': total,
    })


def show_one_director(request, id_director: int):
    director = get_object_or_404(Director, id=id_director)
    return render(request, 'movieapp/one_director.html', {
        'director': director,
    })
