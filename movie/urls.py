from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('search', views.search, name='search'),
    path('type', views.getType, name='type'),
    path('movie/<int:id>', views.getMovieById, name='movie'),
    path('watchmovie/<int:id>', views.watchMovie),
]
