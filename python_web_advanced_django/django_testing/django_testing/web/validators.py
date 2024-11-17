from django.core.exceptions import ValidationError


def check_name_contains_only_letters(value):
    if not value.isalpha():
        raise ValidationError("Name must contain only letters!")


def check_username_containes_only_alphanumerics(value):
    if not value.isalnum():
        raise ValidationError("Username must contain only alphanumeric characters")