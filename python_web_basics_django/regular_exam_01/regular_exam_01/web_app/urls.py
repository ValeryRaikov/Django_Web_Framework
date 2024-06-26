from django.urls import path
from regular_exam_01.web_app.views import (show_home, album_add, album_details, album_edit, album_delete,
                                           profile_details, profile_create, profile_edit, profile_delete)

urlpatterns = [
    path('', show_home, name='show home'),
    path('album/add/', album_add, name='album add'),
    path('album/details/<int:pk>/', album_details, name='album details'),
    path('album/edit/<int:pk>/', album_edit, name='album edit'),
    path('album/delete/<int:pk>/', album_delete, name='album delete'),
    path('profile/details/', profile_details, name='profile details'),
    path('profile/create/', profile_create, name='profile create'),
    path('profile/edit/', profile_edit, name='profile edit'),
    path('profile/delete/', profile_delete, name='profile delete'),
]