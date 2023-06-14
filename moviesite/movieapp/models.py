from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.core.validators import MinValueValidator, MaxValueValidator


class Director(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    director_email = models.EmailField()

    def get_url(self):
        return reverse('director-detail', args=[self.id])

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Actor(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    GENDERS = [
        (MALE, 'Мужчина'),
        (FEMALE, 'Женщина'),
    ]
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDERS, default=MALE)
    slug = models.SlugField(default='',
                            null=False,
                            db_index=True,
                            blank=True)

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.last_name + self.first_name)
    #     super(Actor, self).save(*args, **kwargs)

    def get_url(self):
        return reverse('actor-detail', args=[self.slug])

    def __str__(self):
        label = 'Актер' if self.gender == self.MALE else 'Актриса'
        return f'{label} {self.first_name} {self.last_name}'

class Movie(models.Model):
    EURO = 'EUR'
    USD = 'USD'
    RUB = 'RUB'
    CURRENCY_CHOICES = [
        (EURO, 'Euro'),
        (USD, 'Dollar'),
        (RUB, 'Rubles')
        ]
    name = models.CharField(max_length=40)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    year = models.IntegerField(null=True, blank=True)
    budget = models.IntegerField(null=True)
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default=RUB)
    slug = models.SlugField(default='',
                            null=False,
                            db_index=True,
                            blank=True)# для быстрого поиска в DB
    director = models.ForeignKey(Director, on_delete=models.PROTECT, null=True)
    actors = models.ManyToManyField(Actor)

    def get_url(self):
        return reverse('movie-detail', args=[self.slug])

    def __str__(self):
        return f"{self.name}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Movie, self).save(*args, **kwargs)
