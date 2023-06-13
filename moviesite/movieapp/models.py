from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Movie(models.Model):
    name = models.CharField(max_length=40)
    rating = models.IntegerField()
    year = models.IntegerField(null=True)
    budget = models.IntegerField(null=True)
    slug = models.SlugField(default='',
                            null=False,
                            db_index=True) # для быстрого поиска в DB

    def get_url(self):
        return reverse('movie-detail', args=[self.slug])

    def __str__(self):
        return f"{self.name}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Movie, self).save(*args, **kwargs)
