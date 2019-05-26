from django.db import models
from datetime import date


class Movie(models.Model):
    Title = models.CharField(max_length=255)
    Year = models.CharField(max_length=120)
    Rated = models.CharField(max_length=120)
    Released = models.CharField(max_length=120)
    Runtime = models.CharField(max_length=120)
    Genre = models.CharField(max_length=120)
    Director = models.CharField(max_length=120)
    Writer = models.CharField(max_length=120) # 250
    Actors = models.CharField(max_length=120) # 250
    Plot = models.TextField()
    Language = models.CharField(max_length=120)
    Country = models.CharField(max_length=120)
    Awards = models.CharField(max_length=250)
    Poster = models.URLField()
    Ratings = models.TextField()
    Metascore = models.CharField(max_length=120)
    imdbRating = models.CharField(max_length=120)
    imdbVotes = models.CharField(max_length=120)
    imdbID = models.CharField(max_length=120)
    Type = models.CharField(max_length=120)
    totalSeasons = models.CharField(max_length=120)
    DVD = models.CharField(max_length=120)
    BoxOffice = models.CharField(max_length=120)
    Production = models.CharField(max_length=120)
    Website = models.URLField()
    Response = models.CharField(max_length=5)

    def __str__(self):
        return str(self.id)


class Comment(models.Model):
    movie = models.ForeignKey(Movie,
                              on_delete=models.CASCADE,
                              related_name='comments')
    content = models.TextField()
    date_added = models.DateField(default=date.today)
