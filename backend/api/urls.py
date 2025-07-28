from django.urls import path
from . import views

urlpatterns = [
  path('movies/', views.movielist, name="movies"),
  path('movie/<int:id>/', views.movieDetail, name="movie-detail"),
  path('movie-update/<int:id>/', views.movieUpdate, name="movie-update"),
  path('movie-add/', views.addMovie, name="add-movie"),
  path('movie-delete/<int:id>/', views.deleteMovie, name="delete-movie"),
]