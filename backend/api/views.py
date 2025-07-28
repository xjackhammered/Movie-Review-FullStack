from django.shortcuts import render
from rest_framework.response import Response
from .serializers import MovieSerializer, GenreSerializer, ReviewSerializer
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

@api_view(['POST'])
def addMovie(request):
    serializer = MovieSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteMovie(request, id):
    movie = Movie.objects.get(id=id)
    movie.delete()

    return Response("Movie deleted successfully!")

@api_view(['POST'])
def genreAdd(request):
    serializer = GenreSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)

@api_view(['DELETE'])
def genreDelete(request, id):
    genre = Genre.objects.get(id=id)
    genre.delete()

    return Response("Genre successfully deleted")

@api_view(['GET'])
def genreList(request):
    genre = Genre.objects.all()
    serializer = GenreSerializer(genre, many=True)
    
    return Response(serializer.data)


@api_view(['GET'])
def reviewList(request):
    review = Review.objects.all()
    serializer = ReviewSerializer(review, many=True)
    
    return Response(serializer.data)


@api_view(['DELETE'])
def reviewDelete(request, id):
    review = Review.objects.get(id=id)
    review.delete()

    return Response("Review successfully deleted")

@api_view(['POST'])
def reviewAdd(request):
    serializer = ReviewSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)