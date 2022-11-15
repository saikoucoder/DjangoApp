from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('search', views.search),
    path('type', views.getType),
    path('movie/<int:id>', views.getMovieById),
    path('watchmovie/<int:id>', views.watchMovie),
]
