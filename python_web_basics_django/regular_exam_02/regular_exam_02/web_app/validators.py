from django.core.exceptions import ValidationError


PERSON_NAME_VALIDATION_ERROR_MSG = 'Your name must start with a capital letter!'
PLANT_NAME_VALIDATION_ERROR_MSG = 'Plant name should contain only letters!'

def validate_person_name(value):
    if not value[0].isupper():
        raise ValidationError(PERSON_NAME_VALIDATION_ERROR_MSG)


def validate_plant_name(value):
    if not value.isalpha():
        raise ValidationError(PLANT_NAME_VALIDATION_ERROR_MSG)