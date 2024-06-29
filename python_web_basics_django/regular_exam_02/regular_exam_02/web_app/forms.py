from django import forms
from django.core.validators import MinLengthValidator, MinValueValidator
from regular_exam_02.web_app.validators import validate_person_name, validate_plant_name


class BaseProfileForm(forms.Form):
    USERNAME_MAX_LEN = 10
    USERNAME_MIN_LEN = 2
    NAME_MAX_LEN = 20

    username = forms.CharField(
        max_length=USERNAME_MAX_LEN,
        required=True,
        label='Username:',
        validators=[
            MinLengthValidator(USERNAME_MIN_LEN),
        ],
    )

    first_name = forms.CharField(
        max_length=NAME_MAX_LEN,
        required=True,
        label='First Name:',
        validators=[
            validate_person_name,
        ],
    )

    last_name = forms.CharField(
        max_length=NAME_MAX_LEN,
        required=True,
        label='Last Name:',
        validators=[
            validate_person_name,
        ],
    )


class CreateProfileForm(BaseProfileForm):
    pass


class EditProfileForm(BaseProfileForm):
    profile_picture = forms.URLField(
        required=False,
        label='Profile Picture URL:',
    )


class DeleteProfileForm(BaseProfileForm):
    profile_picture = forms.URLField(
        required=False,
        label='Profile Picture URL:',
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].widget.attrs['readonly'] = True
            self.fields[field_name].widget.attrs['disabled'] = True


class BasePlantForm(forms.Form):
    TYPE_MAX_LEN = 14
    NAME_MAX_LEN = 20
    NAME_MIN_LEN = 2

    PLANT_TYPES = [
        ('OP', 'Outdoor Plants'),
        ('IP', 'Indoor Plants'),
    ]

    type = forms.ChoiceField(
        choices=PLANT_TYPES,
        required=True,
        label='Plant type:',
    )

    name = forms.CharField(
        max_length=NAME_MAX_LEN,
        required=True,
        label='Plant name:',
        validators=[
            MinLengthValidator(NAME_MIN_LEN),
            validate_plant_name,
        ],
    )

    image_url = forms.URLField(
        required=True,
        label='Plant image URL:',
    )

    description = forms.CharField(
        widget=forms.Textarea,
        required=True,
        label='Description:',
    )

    price = forms.FloatField(
        required=True,
        label='Price:',
        validators=[
            MinValueValidator(0),
        ],
    )


class CreatePlantForm(BasePlantForm):
    pass


class EditPlantForm(BasePlantForm):
    pass


class DeletePlantForm(BasePlantForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].widget.attrs['readonly'] = True
            self.fields[field_name].widget.attrs['disabled'] = True
