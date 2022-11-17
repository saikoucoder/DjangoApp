from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('search', views.search),
    path('type', views.getType),
    path('movie/<int:id>', views.getMovieById, name="movie"),
    path('watchmovie/<int:id>', views.watchMovie),
]
