import random

from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render, redirect
from django.views.generic import TemplateView


# Function-based views
def home(request):
    return HttpResponse('This is home.')


def department(request):
    return HttpResponse(
        f'This is department. Method -> {request.method}',
        content_type='text/plain',
    )


def more(request, id):
    return HttpResponse(f'This is more page with index: {id}')


def bad_request(request):
    return HttpResponse(HttpResponseBadRequest)  # == return HttpResponse(status=404)


def go_to_home(request):
    return redirect('/')


def html(request):
    name = input('Enter your name: ')

    context = {
        'name': name,
        'numbers': sorted([random.randint(1, 1000) for _ in range(10)]),
    }

    return render(
        request,
        'index.html',
        context,
        content_type='text/html',
    )


def html_with_css(request):
    return render(request, 'layout.html')


# Class-based views
# class HomeView(TemplateView):
#     template_name = 'index.html'
