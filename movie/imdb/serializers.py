from rest_framework import serializers

from .models import Movie, Genre

class MovieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'name', 'imdb_score', 'popularity', 'director')