from django.contrib import admin
from .models import Movie


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['name', 'rating', 'year', 'currency', 'budget', 'slug', 'rating_status']
    list_editable = ['rating', 'year', 'currency', 'budget']
    ordering = ['-rating', 'name']
    list_per_page = 15

    @admin.display(ordering='rating', description='статус')
    def rating_status(self, movie: Movie):
        if movie.rating < 70:
            return 'Зачем это смотреть'
        if movie.rating < 80:
            return 'Разок можно глянуть'
        if movie.rating < 85:
            return 'Зачет'
        return 'Топчик'
