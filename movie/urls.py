from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='home'),
    path('search', views.search, name='search'),
    path('type', views.getType, name='type'),
    path('movie/<int:id>', views.getMovieById, name='movie'),
    path('watchmovie/<int:id>', views.watchMovie, name='watchmovie'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name="pages/login.html"), name="login"),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name="logout"),
]
