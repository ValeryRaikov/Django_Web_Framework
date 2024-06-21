from django.db import models
from django.core import validators

class Department(models.Model):
    class Location(models.TextChoices):
        SOFIA = 'Sofia', 'Sofia'
        VARNA = 'Varna', 'Varna'
        PLOVDIV = 'Plovdiv', 'Plovdiv'
        PLEVEN = 'Pleven', 'Pleven'


    name = models.CharField(
        max_length=100,
        null=False,
        blank=False,
    )

    location = models.CharField(
        max_length=max(len(l) for l in (Location.SOFIA, Location.VARNA, Location.PLOVDIV, Location.PLEVEN)),
        choices=Location.choices,
        default=Location.SOFIA,
    )

    users_count = models.PositiveIntegerField(
        null=False,
        blank=False,
    )

    def __str__(self):
        return f'Department {self.name} located in {self.location}'


class User(models.Model):
    first_name = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        validators=[
            validators.MinLengthValidator(2),
        ],
    )

    last_name = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        validators=[
            validators.MinLengthValidator(2),
        ],
    )

    username = models.CharField(
        max_length=25,
        null=False,
        blank=False,
        unique=True,
    )

    email = models.EmailField(
        null=False,
        blank=False,
        unique=True,
    )

    password = models.CharField(
        max_length=16,
        null=False,
        blank=False,
        unique=True,
        validators=[
            validators.MinLengthValidator(6),
        ],
    )

    job_department = models.ForeignKey(
        to=Department,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f'User {self.first_name} {self.last_name}'
