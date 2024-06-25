from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible

VALIDATE_LETTERS_EXCEPTION_MSG = 'Ensure this value contains only letters.'
VALIDATE_MAX_FILE_SIZE_MSG = 'Max file size is 5.00 MB.'

def validate_only_letters(value):
    if not all(c.isalpha() for c in value):
        raise ValidationError(VALIDATE_LETTERS_EXCEPTION_MSG)


@deconstructible
class ValidateMaxFileSize:
    def __init__(self, max_size):
        self.max_size = max_size

    def __call__(self, value):
        filesize = value.file.size
        if filesize > self.max_size * 1024 * 1024:
            raise ValidationError(VALIDATE_MAX_FILE_SIZE_MSG)