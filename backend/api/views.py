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

@api_view(['GET'])
def movieDetail(request, id):
    movie = Movie.objects.get(id=id)
    serializer = MovieSerializer(movie, many=False)
    return Response(serializer.data)

@api_view(['POST', 'PATCH'])
def movieUpdate(request, id):
    movie = Movie.objects.get(id=id)

    partial = request.method == "PATCH"
    serializer = MovieSerializer(instance=movie, data=request.data, partial=partial)

    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)