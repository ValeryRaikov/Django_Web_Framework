from django.shortcuts import render, redirect
from django import forms

from django.core.exceptions import ValidationError
from django_forms.forms_app.models import User, Department


def validate_positive(value):
    if value < 0:
        raise ValidationError('Value must be greater than 0!')


# class UserForm(forms.Form):
#     first_name = forms.CharField(
#         max_length=50,
#         label='Enter first name',
#         widget=forms.TextInput(
#             attrs={
#                 'class': 'form-control', # Just for test purpose
#             }
#         )
#     )
#
#     last_name = forms.CharField(
#         max_length=50,
#     )
#
#     age = forms.IntegerField(
#         required=False,
#         validators=[
#             validate_positive,
#         ]
#     )

# Model Forms
class UserForm(forms.ModelForm):
    bot_catcher = forms.CharField(
        widget=forms.HiddenInput(),
        required=False,
    )

    def clean_bot_catcher(self):
        value = self.cleaned_data['bot_catcher']

        if value:
            raise ValidationError('Bot found!')

    class Meta:
        model = User
        fields = '__all__'


class EditUserForm(UserForm):
    def clean(self):
        pass # Add logic here

    class Meta:
        model = User
        fields = '__all__'
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'readonly': 'readonly',
                },
            ),

            'job_department': forms.TextInput(
                attrs={
                    'readonly': 'readonly',
                },
            ),
        }


class DepartmentForm(forms.Form):
    name = forms.CharField(
        max_length=100,
    )

    location = forms.ChoiceField(
        choices=(
            ('Sofia', 'Sofia'),
            ('Varna', 'Varna'),
            ('Plovdiv', 'Plovdiv'),
            ('Pleven', 'Pleven'),
        )
    )


def default(request):
    context = {}

    return render(request, 'index.html', context)


def unbound_forms(request):
    context = {}

    return render(request, 'unbound_forms.html', context)


def bound_forms(request):
    context = {
        'user_form': UserForm(),
    }

    return render(request, 'bound_forms.html', context)


# @require_http_methods(["GET", "POST"]) -> decorator
def create_user(request):
    # print(request.method)
    # print(request.GET)

    user_form = UserForm(request.POST)

    is_valid = False
    if user_form.is_valid():
        is_valid = True

    context = {
        'is_valid': is_valid,
        'user_form': user_form,
    }

    return render(request, 'bound_forms.html', context)


def manage_user(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)

        if user_form.is_valid():
            user = User(
                **user_form.cleaned_data,
            )
            # when working with model forms
            user.save()
            user_form.save()

            return redirect('default')
    else:
        user_form = UserForm()

    context = {
        'user_form': user_form,
    }

    return render(request, 'create.html', context)


def create_department(request):
    if request.method == 'POST':
        department_form = DepartmentForm(request.POST)

        if department_form.is_valid():
            department = Department(
                **department_form.cleaned_data,
            )
            department.save()

            return redirect('default')
    else:
        department_form = DepartmentForm()

    context = {
        'department_form': department_form,
    }

    return render(request, 'create_department.html', context)


def edit_user(request, pk):
    user = User.objects.get(pk=pk)

    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=user)

        if user_form.is_valid():
            user_form.save()
    else:
        user_form = UserForm(instance=user)

    context = {
        'user': user,
        'user_form': user_form,
    }

    return render(request, 'edit_user.html', context)
