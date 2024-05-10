import random

from django.shortcuts import render, redirect

from models_demo.vehicles.models import Dealership, VehicleOwner


def home(request):
    return render(request, 'default.html')


def hello(request):
    name = input('Enter your name: ')
    age = input('Enter your age: ')

    context = {
        'name': name,
        'age': age
    }

    return render(request, 'hello.html', context)


def generate_random_nums(request):
    context = {
        'numbers': [random.randint(1, 50) for _ in range(6)]
    }

    return render(request, 'lottery.html', context)


def display_dealerships(request):
    filtered_dealerships = Dealership.objects.filter(location='Sofia').order_by('name')

    context = {
        'dealerships': Dealership.objects.all(),
        'filtered_dealerships': filtered_dealerships
    }

    return render(request, 'dealerships.html', context)


def display_owners(request):
    context = {
        'owners': VehicleOwner.objects.all().order_by('first_name', 'last_name')
    }

    return render(request, 'owners.html', context)


def navigation(request):
    return render(request, 'site_nav.html')


def styled_page(request):
    context = {
        'owners': VehicleOwner.objects.all()
    }

    return render(request, 'styled.html', context)


def test_filters(request):
    context = {
        'text': 'HelLO TheRE, HoW arE yOU?',
        'text2': 'AnOThEr TeST stRiNG',
        'number': 10,
        'number2': 81,
        'number3': -5
    }

    return render(request, 'filters.html', context)
