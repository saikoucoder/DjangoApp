from urllib import response
from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie
# Create your views here.


def index(request):
    Data = {"Movies": Movie.objects.all()}
    return render(request, "pages/home.html", Data)


def getMovieById(request, id):
    movie = Movie.objects.get(id=id)
    return render(request, "pages/movie.html", {'movie': movie, 'n': range(movie.rating), 'm': range(5-movie.rating)})
