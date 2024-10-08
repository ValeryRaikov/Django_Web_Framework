from django.contrib.auth import get_user_model
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, Group, Permission
from django.db import models

from auth_demo.auth_app.managers import AppUsersManager

UserModel = get_user_model()


# class UserProxy(UserModel):
#     class Meta:
#         proxy = True
#         ordering = ['first_name',]
#
#     @property
#     def full_name(self):
#         return f'{self.first_name} {self.last_name}'


class AppUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        unique=True,
        null=False,
        blank=False,
    )

    is_staff = models.BooleanField(
        default=False,
    )

    date_joined = models.DateTimeField(
        auto_now_add=True,
    )

    USERNAME_FIELD = 'email'

    objects = AppUsersManager()

    groups = models.ManyToManyField(
        Group,
        related_name='auth_app_user_set',
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='auth_app_user_set',
        blank=True,
    )


class Profile(models.Model):
    first_name = models.CharField(
        max_length=50,
    )

    last_name = models.CharField(
        max_length=50,
    )

    user = models.OneToOneField(
        to=AppUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )
