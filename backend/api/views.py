from django.shortcuts import render
from rest_framework.response import Response
from .serializers import MovieSerializer
from rest_framework.decorators import api_view
from .models import Movie, Genre, Review

# Create your views here.

@api_view(['GET'])
def movielist(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)