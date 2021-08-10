from django.conf.urls import url
from django.contrib import admin
from .views import (searchmovies)

urlpatterns = [
    url(r'^$', searchmovies, name='searchmovies'),
]