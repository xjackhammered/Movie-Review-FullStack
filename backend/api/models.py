from django.db import models

# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
class Movie(models.Model):
    name = models.CharField(max_length=200, null=False)
    director = models.CharField(max_length=200, null=True, default="Unknown")
    genres = models.ManyToManyField(Genre)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Review(models.Model):
    content = models.TextField(max_length=1000, null=False)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content[0:100]