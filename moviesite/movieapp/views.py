from django.shortcuts import render, get_object_or_404
from .models import Movie, Director, Actor
from django.db.models import F, Avg, Min, Max
from django.views.generic import ListView, DetailView



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


class ListDirectors(ListView):
    template_name = 'movieapp/all_directors.html'
    model = Director
    context_object_name = 'directors'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total'] = Director.objects.all().count()
        return context


def show_all_directors(request):
    directors = Director.objects.order_by(F('first_name').asc(nulls_last=True))
    total = directors.count()
    return render(request, 'movieapp/all_directors.html', {
        'directors': directors,
        'total': total,
    })


class DetailDirector(DetailView):
    template_name = 'movieapp/one_director.html'
    model = Director
    context_object_name = 'director'


def show_one_director(request, id_director: int):
    director = get_object_or_404(Director, id=id_director)
    return render(request, 'movieapp/one_director.html', {
        'director': director,
    })


class ListActors(ListView):
    template_name = 'movieapp/all_actors.html'
    model = Actor
    context_object_name = 'actors'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total'] = Actor.objects.all().count()
        return context

def show_all_actors(request):
    actors = Actor.objects.order_by(F('first_name').asc(nulls_last=True))
    total = actors.count()
    return render(request, 'movieapp/all_actors.html', {
        'actors': actors,
        'total': total,
    })


class DetailActor(DetailView):
    template_name = 'movieapp/one_actor.html'
    model = Actor
    context_object_name = 'actor'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['context'] = 'Актер' if kwargs['object'].gender == kwargs['object'].MALE else 'Актриса'
        return context

def show_one_actor(request, slug_actor: str):
    actor = get_object_or_404(Actor, slug=slug_actor)
    context = 'Актер' if actor.gender == actor.MALE else 'Актриса'
    return render(request, 'movieapp/one_actor.html', {
        'actor': actor,
        'context': context
    })
