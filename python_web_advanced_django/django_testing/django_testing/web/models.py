from django.db import models
from .validators import check_name_contains_only_letters, check_username_containes_only_alphanumerics


class Profile(models.Model):
    NAME_MAX_LEN = 50

    first_name = models.CharField(
        max_length=NAME_MAX_LEN,
        validators=[
            check_name_contains_only_letters,
        ],
    )

    last_name = models.CharField(
        max_length=NAME_MAX_LEN,
        validators= [
            check_name_contains_only_letters,
        ],
    )

    email = models.EmailField(
        null=True,
        blank=True,
    )

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'


class Account(models.Model):
    USERNAME_MAX_LEN = 25
    PASSWORD_MAX_LEN = 16

    username = models.CharField(
        max_length=USERNAME_MAX_LEN,
        validators= [
            check_username_containes_only_alphanumerics,
        ],
    )

    password = models.CharField(
        max_length=PASSWORD_MAX_LEN,
    )

    is_banned = models.BooleanField(
        default=False,
        null=True,
        blank=True,
    )

    profile = models.OneToOneField(
        to=Profile,
        on_delete=models.CASCADE,
    )
