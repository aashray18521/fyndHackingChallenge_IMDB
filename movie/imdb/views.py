from rest_framework import viewsets

from .serializers import MovieSerializer
from .models import Movie

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all().order_by('name')
    serializer_class = MovieSerializer