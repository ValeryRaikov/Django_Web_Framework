import os

from django import forms
from exam_preparation.expense_tracker.models import Profile, Expense

class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class DeleteProfileForm(forms.ModelForm):
    def save(self, commit=True):
        img_path = self.instance.image.path

        if commit:
            self.instance.delete()
            os.remove(img_path)
            Expense.objects.all().delete()

        return self.instance

    class Meta:
        model = Profile
        fields = '__all__'


class CreateExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = '__all__'


class EditExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = '__all__'


class DeleteExpenseForm(forms.ModelForm):
    def __init__(self, *args, **kwars):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Expense
        fields = '__all__'
