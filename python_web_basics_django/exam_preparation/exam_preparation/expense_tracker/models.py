from django.core import validators
from django.db import models
from exam_preparation.expense_tracker.validators import validate_only_letters, ValidateMaxFileSize

class Profile(models.Model):
    MIN_LEN_NAME = 2
    MAX_LEN_NAME = 15
    BUDGET_DEFAULT = 0
    IMAGE_MAX_SIZE_IN_MB = 5
    IMAGE_UPLOAD_TO_DIR = 'profiles/'

    first_name = models.CharField(
        max_length=MAX_LEN_NAME,
        validators=[
            validators.MinLengthValidator(MIN_LEN_NAME),
            validate_only_letters,
        ],
    )

    last_name = models.CharField(
        max_length=MAX_LEN_NAME,
        validators=[
            validators.MinLengthValidator(MIN_LEN_NAME),
            validate_only_letters,
        ],
    )

    budget = models.FloatField(
        default=BUDGET_DEFAULT,
        validators=[
            validators.MinValueValidator(BUDGET_DEFAULT),
        ],
    )

    image = models.ImageField(
        upload_to=IMAGE_UPLOAD_TO_DIR,
        null=True,
        blank=True,
        validators=[
            ValidateMaxFileSize(IMAGE_MAX_SIZE_IN_MB),
        ],
    )


class Expense(models.Model):
    TITLE_MAX_LEN = 30
    PRICE_DEFAULT = 0

    title = models.CharField(
        max_length=TITLE_MAX_LEN,
    )

    image = models.URLField()

    description = models.TextField(
        null=True,
        blank=True,
    )

    price = models.FloatField(
        default=PRICE_DEFAULT,
        validators=[
            validators.MinValueValidator(PRICE_DEFAULT),
        ],
    )

    class Meta:
        ordering = ('title', 'price',)
