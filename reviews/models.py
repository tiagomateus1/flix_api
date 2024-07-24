from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from movies.models import Movie


class Review(models.Model):
    movie = models.ForeignKey(
        Movie,
        on_delete=models.PROTECT,
        related_name='reviews'
    )
    stars = models.IntegerField(
        validators=[
            MinValueValidator(0, 'Você não pode avaliar com valores abaixo de 0 estrelas.'),
            MaxValueValidator(5, 'Você só pode avaliar até 5 estrelas.'),
        ]
    )
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.movie)
