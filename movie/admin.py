from django.contrib import admin
from .models import Category, Director, Movie, Comment
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'create_date']
    search_fields = ['name']
    list_filter = ['create_date']


class DirectorAdmin(admin.ModelAdmin):
    list_display = ['name', 'nationality', 'create_date']
    search_fields = ['name', 'nationality']
    list_filter = ['create_date']

class CommentInline(admin.StackedInline):
    model = Comment

class MovieAdmin(admin.ModelAdmin):
    list_display = ['name','director','category', 'create_date']
    search_fields = ['name','category']
    list_filter = ['create_date']
    inlines = [CommentInline]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Director, DirectorAdmin)
admin.site.register(Movie, MovieAdmin)
