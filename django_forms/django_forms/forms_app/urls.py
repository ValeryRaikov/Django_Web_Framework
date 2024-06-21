from django.urls import path

from django_forms.forms_app.views import (default, unbound_forms, bound_forms, create_user, manage_user,
                                          create_department, edit_user)

urlpatterns = [
    path('', default, name='default'),
    path('unbound/', unbound_forms, name='unbound'),
    path('bound/', bound_forms, name='bound'),
    path('create/', create_user, name='create user'),
    path('manage/', manage_user, name='manage user'),
    path('create_dep/', create_department, name='create department'),
    path('edit_user/<int:pk>/', edit_user, name='edit user'),
]