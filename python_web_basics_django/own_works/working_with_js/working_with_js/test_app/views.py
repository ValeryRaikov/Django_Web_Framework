import time

from django.forms import model_to_dict
from django.http import JsonResponse
from django.shortcuts import render, redirect

from working_with_js.test_app.forms import PersonForm
from working_with_js.test_app.models import Person, Department


def get_all_departments():
    return Department.objects.all()


def get_all_people():
    return Person.objects.all()


def show_index(request):
    departments = get_all_departments()
    people = get_all_people()

    context = {
        'departments': departments,
        'people': people,
    }

    return render(request, 'index.html', context)


def show_departments(request):
    departments = get_all_departments()

    context = {
        'departments': [model_to_dict(d) for d in departments],
    }

    return JsonResponse(context)


def show_people(request):
    people = get_all_people()

    context = {
        'people': [model_to_dict(p) for p in people]
    }

    time.sleep(3)

    return JsonResponse(context)


def register_person(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('show index')
    else:
        form = PersonForm()

    context = {
        'form': form,
    }

    return render(request, 'register_person.html', context)


def show_all_simple(request):
    departments = get_all_departments()
    people = get_all_people()

    context = {
        'departments': departments,
        'people': people,
    }

    return render(request, 'show_all.html', context)
