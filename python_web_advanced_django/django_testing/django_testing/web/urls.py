from django.urls import path
from .views import ProfileCreateView, ProfileListView, ProfileDetailsView

urlpatterns = [
    path('', ProfileListView.as_view(), name='list profiles'),
    path('create/', ProfileCreateView.as_view(), name='create profile'),
    path('details/<int:pk>', ProfileDetailsView.as_view(), name='profile details'),
]
