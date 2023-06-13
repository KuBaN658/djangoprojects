from django.contrib import admin, messages
from .models import Movie
from django.db.models import QuerySet


class RatingFilter(admin.SimpleListFilter):
    title = 'Фильтр по рейтингу'
    parameter_name = 'rating'

    def lookups(self, request, model_admin):
        return [
            ('< 70', 'Низкий'),
            ('от 70 до 80', 'средний'),
            ('>80', 'высокий')
        ]

    def queryset(self, request, queryset: QuerySet):
        if self.value() == '< 70':
            return queryset.filter(rating__lt=70)
        if self.value() == 'от 70 до 80':
            return queryset.filter(rating__lte=80)
        return queryset.filter(rating__gt=80)


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['name', 'rating', 'year', 'currency', 'budget', 'slug', 'rating_status']
    list_editable = ['rating', 'year', 'currency', 'budget']
    ordering = ['-rating', 'name']
    list_per_page = 15
    actions = ['set_dollars']
    search_fields = ['name']  # поле поиска name__startswith - совпадения только сначала
    list_filter = ['currency', RatingFilter]

    @admin.display(ordering='rating', description='статус')
    def rating_status(self, movie: Movie):
        if movie.rating < 70:
            return 'Зачем это смотреть'
        if movie.rating < 80:
            return 'Разок можно глянуть'
        if movie.rating < 85:
            return 'Зачет'
        return 'Топчик'

    @admin.action(description='установить валюту - Доллар')
    def set_dollars(self, request, qs: QuerySet):
        count_updated = qs.update(currency=Movie.USD)
        self.message_user(
            request,
            f'было обновлено {count_updated} записей!',
            messages.WARNING
        )
