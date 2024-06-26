import re

from django.core import validators
from django.core.exceptions import ValidationError
from django.db import models

VALIDATE_USERNAME_ERROR_MSG = 'Ensure this value contains only letters, numbers, and underscore.'


def validate_username_correct_pattern(value):
    if not re.match(r'^\w+$', value):
        raise ValidationError(VALIDATE_USERNAME_ERROR_MSG)


class Profile(models.Model):
    USERNAME_MAX_LEN = 15
    USERNAME_MIN_LEN = 2

    username = models.CharField(
        max_length=USERNAME_MAX_LEN,
        validators=[
            validators.MinValueValidator(USERNAME_MIN_LEN),
        ],
    )

    email = models.EmailField()

    age = models.PositiveIntegerField(
        null=True,
        blank=True,
    )

    def __str__(self):
        return f'User: {self.username}'


class Album(models.Model):
    NAME_MAX_LEN = 30
    ARTIST_MAX_LEN = 30
    MIN_PRICE_VALUE = 0

    class Genres(models.TextChoices):
        POP = 'Pop Music'
        JAZZ = 'Jazz Music'
        R_B = 'R&B Music'
        ROCK = 'Rock Music'
        COUNTRY = 'Country Music'
        DANCE = 'Dance Music'
        HIP_HOP = 'Hip Hop Music'
        OTHER = 'Other'

    name = models.CharField(
        max_length=NAME_MAX_LEN,
        unique=True,
    )

    artist = models.CharField(
        max_length=ARTIST_MAX_LEN,
    )

    genre = models.CharField(
        max_length=max(len(g) for g in (Genres.POP, Genres.JAZZ, Genres.R_B, Genres.ROCK, Genres.COUNTRY, Genres.DANCE,
                                        Genres.HIP_HOP, Genres.OTHER)),
        choices=Genres.choices,
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    image_url = models.URLField()

    price = models.FloatField(
        validators=[
            validators.MinValueValidator(MIN_PRICE_VALUE),
        ],
    )

    def __str__(self):
        return f'Album: {self.name}'
