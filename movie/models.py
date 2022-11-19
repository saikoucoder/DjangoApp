from django.db import models
from django.conf import settings

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Director(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to="images")
    nationality = models.CharField(max_length=200)
    birthday = models.DateField()
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Movie(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to="images/movie")
    plot = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    release_year = models.DateField()
    rating = models.IntegerField()
    movie_length = models.IntegerField()
    create_date = models.DateTimeField(auto_now_add=True)
    video_url = models.CharField(max_length=400, null=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    movie = models.ForeignKey(
        Movie, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
