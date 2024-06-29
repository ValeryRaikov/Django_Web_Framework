from django.db import models
from django.core import validators
from regular_exam_02.web_app.validators import validate_person_name, validate_plant_name


class Profile(models.Model):
    USERNAME_MAX_LEN = 10
    USERNAME_MIN_LEN = 2
    NAME_MAX_LEN = 20

    username = models.CharField(
        max_length=USERNAME_MAX_LEN,
        null=False,
        blank=False,
        verbose_name='Username:',
        validators=[
            validators.MinLengthValidator(USERNAME_MIN_LEN),
        ],
    )

    first_name = models.CharField(
        max_length=NAME_MAX_LEN,
        null=False,
        blank=False,
        verbose_name='First Name:',
        validators=[
            validate_person_name,
        ],
    )

    last_name = models.CharField(
        max_length=NAME_MAX_LEN,
        null=False,
        blank=False,
        verbose_name='Last Name:',
        validators=[
            validate_person_name,
        ],
    )

    profile_picture = models.URLField(
        null=True,
        blank=True,
        verbose_name='Profile Picture URL:',
    )

    def __str__(self):
        return f'Profile: {self.username}'


class Plant(models.Model):
    TYPE_MAX_LEN = 14
    NAME_MAX_LEN = 20
    NAME_MIN_LEN = 2

    class PlantTypes(models.TextChoices):
        OP = 'Outdoor Plants'
        IP = 'Indoor Plants'

    type = models.CharField(
        max_length=TYPE_MAX_LEN,
        null=False,
        blank=False,
        verbose_name='Plant type:',
        choices=PlantTypes.choices,
    )

    name = models.CharField(
        max_length=NAME_MAX_LEN,
        null=False,
        blank=False,
        verbose_name='Plant name:',
        validators=[
            validators.MinLengthValidator(NAME_MIN_LEN),
            validate_plant_name,
        ],
    )

    image_url = models.URLField(
        null=False,
        blank=False,
        verbose_name='Plant image URL:',
    )

    description = models.TextField(
        null=False,
        blank=False,
        verbose_name='Description:',
    )

    price = models.FloatField(
        null=False,
        blank=False,
        verbose_name='Price:',
        validators=[
            validators.MinValueValidator(0),
        ],
    )

    def __str__(self):
        return f'Plant: {self.name}'
