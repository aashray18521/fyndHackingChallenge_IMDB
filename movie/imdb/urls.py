from django.urls import path

from imdb.views import MoviesList

urlpatterns = [
    path('movies', MoviesList.as_view(), name='movies'),
]
