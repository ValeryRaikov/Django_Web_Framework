from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    # Bad practice -> Use template instead!
    html_greet = f"""
    <h1>Hello from HTML</h1>
    <p>This is awesome!</p>
    """

    return HttpResponse('It works!\n' + html_greet)


def hello(request):
    context = {
        'title': 'It works well again!'
    }

    return render(request, 'hello.html', context)
