from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=200)
    budget = models.IntegerField()
    homepage = models.
    overview = models
    popularity
    release_date