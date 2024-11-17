from django import forms
from django.forms import modelform_factory
from .models import Profile, Account


ProfileForm = modelform_factory(Profile, fields='__all__')
AccoutForm = modelform_factory(Account, fields='__all__')
