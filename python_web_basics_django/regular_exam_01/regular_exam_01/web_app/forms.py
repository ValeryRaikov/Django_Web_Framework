from django import forms

from regular_exam_01.web_app.models import Album, Profile


class BaseAlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'
        labels = {
            'name': 'Album Name:',
            'artist': 'Artist:',
            'genre': 'Genre:',
            'description': 'Description:',
            'image_url': 'Image URL:',
            'price': 'Price:',
        }


class AddAlbumForm(BaseAlbumForm):
    pass


class EditAlbumForm(BaseAlbumForm):
    pass


class DeleteAlbumForm(BaseAlbumForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'

    def save(self, commit=True):
        self.instance.delete()

        return self.instance


class BaseProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        labels = {
            'username': 'Username:',
            'email': 'Email:',
            'age': 'Age:',
        }


class CreateProfileForm(BaseProfileForm):
    pass


class EditProfileForm(BaseProfileForm):
    pass


class DeleteProfileForm(BaseProfileForm):
    def save(self, commit=True):
        self.instance.delete()
        Album.objects.all().delete()  # This is done because we suppose there is only one profile!

        return self.instance
