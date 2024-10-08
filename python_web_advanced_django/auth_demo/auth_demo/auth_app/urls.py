from django.urls import path

from auth_demo.auth_app.views import UserRegistrationView, index, UserLoginView, UserLogoutView

urlpatterns = [
    path('', index, name='home'),
    path('register/', UserRegistrationView.as_view(), name='register user'),
    path('login/', UserLoginView.as_view(), name='login user'),
    path('logout/', UserLogoutView.as_view(), name='logout user'),
]
