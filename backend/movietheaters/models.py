from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.

class MovieTheater(models.Model):
    number = models.PositiveSmallIntegerField(validators=[MaxValueValidator(30)], primary_key=True)

    def __str__(self):
        return f'{self.number}'


class Seat(models.Model):
    number = models.PositiveSmallIntegerField(validators=[MaxValueValidator(50)])
    row = models.PositiveSmallIntegerField(validators=[MaxValueValidator(25)])
    movietheater = models.ForeignKey('movietheaters.MovieTheater', related_name='seats', on_delete=models.CASCADE, null=True)

    class Meta:
        unique_together = ['number', 'row', 'movietheater']

    def __str__(self):
        return f'{self.number} - {self.row}'