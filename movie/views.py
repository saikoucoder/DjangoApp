from urllib import response
from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie
# Create your views here.


def index(request):
    Data = {"Movies": Movie.objects.all()}
    return render(request, "pages/home.html", Data)
