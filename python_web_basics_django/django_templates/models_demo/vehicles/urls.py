from django.urls import path

from models_demo.vehicles.views import (home, hello, generate_random_nums, display_dealerships, display_owners,
                                        navigation, styled_page, test_filters)


urlpatterns = [
    path('', home, name='home'),
    path('hello/', hello, name='hello'),
    path('numbers/', generate_random_nums, name='numbers'),
    path('dealers/', display_dealerships, name='dealers'),
    path('owners/', display_owners, name='owners'),
    path('nav/', navigation),
    path('styled/', styled_page),
    path('filters/', test_filters),
]
