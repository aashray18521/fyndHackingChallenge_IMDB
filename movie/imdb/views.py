from rest_framework import generics
from rest_framework.pagination import LimitOffsetPagination
from rest_framework import filters

from imdb.models import Movie
from imdb.serializers import MovieSerializer


class MoviesList(generics.ListAPIView):
    """
    ListAPI view for searching movies.
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'director', 'popularity', 'imdb_score']
