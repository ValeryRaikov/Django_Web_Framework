from django import forms

from working_with_js.test_app.models import Person


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'age', 'email', 'department',]
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'age': 'Age',
            'email': 'Email',
            'department': 'Department',
        }
