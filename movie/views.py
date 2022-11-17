from urllib import response
from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie
from django.db.models import Q
# Create your views here.


def index(request):
    Data = {"Movies": Movie.objects.all()}
    return render(request, "pages/home.html", Data)


def search(request):
    if request.method == 'GET':
        search = request.GET.get('search')
        Data = Movie.objects.filter(Q(name__icontains=search))
        return render(request, "pages/search.html", {'Movies': Data, 'search': search})
    else:
        return render(request, "pages/home.html", {})


def getMovieById(request, id):
    movie = Movie.objects.get(id=id)
    return render(request, "pages/movie.html", {'movie': movie, 'n': range(movie.rating), 'm': range(5-movie.rating)})

def watchMovie(request, id):
    movie = Movie.objects.get(id=id)
    data = Movie.objects.all().order_by("-rating").values()
    return  render(request, "pages/watchmovie.html", {'movie': movie, 'Movies': data})

def getType(request):
    if request.method == 'GET':
        type = request.GET.get('type')
        Data = Movie.objects.filter(category__name=type)
        return render(request, "pages/typemovie.html", {'Movies': Data, 'type': type})
    else:
        return render(request, "pages/home.html", {})