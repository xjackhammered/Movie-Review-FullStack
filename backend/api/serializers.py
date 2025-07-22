from rest_framework import serializers
from .models import Genre, Movie, Review

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    movie = serializers.StringRelatedField(read_only=True)

    movie_id = serializers.PrimaryKeyRelatedField(
        queryset = Movie.objects.all(),
        write_only = True,
        source = 'movie'
    )

    class Meta:
        model = Review
        fields = ['id', 'content', 'rating', 'movie', 'movie_id', 'created_at']



class MovieSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True, read_only=True)

    genre_ids = serializers.PrimaryKeyRelatedField(
        queryset = Genre.objects.all(),
        many=True,
        write_only=True,
        source = 'genres'
    )

    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = ['id', 'name', 'director', 'genres', 'genre_ids', 'created_at', 'reviews']

    
