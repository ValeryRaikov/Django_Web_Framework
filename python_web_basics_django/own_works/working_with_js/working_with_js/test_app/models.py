from django.core import validators
from django.db import models


class Department(models.Model):
    NAME_MAX_LEN = 50
    NAME_MIN_LEN = 5
    MIN_BUDGET_VALUE = 10000

    SOFIA = 'Sofia'
    PLOVDIV = 'Plovdiv'
    VARNA = 'Varna'

    LOCATION_CHOICES = [
        (SOFIA, 'Sofia'),
        (PLOVDIV, 'Plovdiv'),
        (VARNA, 'Varna'),
    ]

    name = models.CharField(
        max_length=50,
        validators=[
            validators.MinLengthValidator(NAME_MIN_LEN),
        ],
    )

    location = models.CharField(
        max_length=max(len(l) for l in (SOFIA, PLOVDIV, VARNA)),
        choices=LOCATION_CHOICES,
    )

    employees_count = models.PositiveIntegerField()

    budget = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        validators=[
            validators.MinValueValidator(MIN_BUDGET_VALUE)
        ]
    )

    def __str__(self):
        return f'Department: {self.name}, {self.location}'


class Person(models.Model):
    NAME_MAX_LEN = 30
    NAME_MIN_LEN = 2
    AGE_MAX_VALUE = 110

    first_name = models.CharField(
        max_length=NAME_MAX_LEN,
        validators=[
            validators.MinLengthValidator(NAME_MIN_LEN),
        ],
    )

    last_name = models.CharField(
        max_length=NAME_MAX_LEN,
        validators=[
            validators.MinLengthValidator(NAME_MIN_LEN),
        ],
    )

    age = models.PositiveIntegerField(
        validators=[
            validators.MinValueValidator(AGE_MAX_VALUE),
        ],
    )

    email = models.EmailField(
        unique=True,
    )

    department = models.ForeignKey(
        to=Department,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f'Person: {self.first_name} {self.last_name}, {self.age}'
