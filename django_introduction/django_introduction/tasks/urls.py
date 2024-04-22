from django.urls import path

from django_introduction.tasks.views import home, hello

urlpatterns = [
    path('', home),
    path('hello/', hello),
]
