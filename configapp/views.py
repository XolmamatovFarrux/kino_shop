from django.shortcuts import render

from configapp.models import Movie, Actor


def index(request):
    movies = Movie.objects.all()
    actors = Actor.objects.all()
    context = {
        'movies': movies,
        'actors': actors
    }

    return render(request, 'movie.html', context=context)


def actor(request):
    movies = Movie.objects.all()
    actors = Actor.objects.all()
    context = {
        'movies': movies,
        'actors': actors
    }
    return render(request, 'actor.html', context=context)
# https://github.com/X  olmamatovFarrux/kino_shop