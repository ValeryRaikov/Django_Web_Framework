from django.urls import path

from regular_exam_02.web_app.views import (show_index, create_profile, profile_details, edit_profile, delete_profile,
                                           show_catalogue, create_plant, plant_details, edit_plant, delete_plant)


urlpatterns = [
    path('', show_index, name='show index'),
    path('profile/create/', create_profile, name='create profile'),
    path('profile/details/', profile_details, name='profile details'),
    path('profile/edit/', edit_profile, name='edit profile'),
    path('profile/delete/', delete_profile, name='delete profile'),
    path('catalogue/', show_catalogue, name='show catalogue'),
    path('create/', create_plant, name='create plant'),
    path('details/<int:pk>/', plant_details, name='plant details'),
    path('edit/<int:pk>/', edit_plant, name='edit plant'),
    path('delete/<int:pk>/', delete_plant, name='delete plant'),
]