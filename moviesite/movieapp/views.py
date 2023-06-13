from django.shortcuts import render, get_object_or_404
from .models import Movie
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
