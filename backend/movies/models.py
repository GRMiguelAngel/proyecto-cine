from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=100)
    duration = models.DurationField()
    genre = models.ForeignKey('movies.Genre', related_name='movies', on_delete=models.PROTECT)
    
    def __str__(self):
        return self.title
    
class Genre(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.name