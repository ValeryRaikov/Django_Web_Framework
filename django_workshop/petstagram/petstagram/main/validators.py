from django.core.exceptions import ValidationError


def only_letters_validator(value):
    for char in value:
        if not char.isalpha():
            raise ValidationError('Value must contain letters only!')


def file_max_size_validator(max_size):
    def validate(value):
        filesize = value.file.size

        if filesize > max_size * 1024 * 1024:
            raise ValidationError(f'Max file size is {max_size}MB')

    return validate
