from django.shortcuts import render, redirect, get_object_or_404

from regular_exam_02.web_app.models import Profile, Plant
from regular_exam_02.web_app.forms import (CreateProfileForm, EditProfileForm, DeleteProfileForm, CreatePlantForm,
                                           EditPlantForm, DeletePlantForm)


def get_profile():
    profiles = Profile.objects.all()

    if not profiles:
        return None

    return profiles[0]


def show_index(request):
    profile = get_profile()

    if not profile:
        return redirect('create profile')

    context = {
        'profile': profile,
    }

    return render(request, 'profile/home-page.html', context)


def create_profile(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            profile = Profile(
                username=form.cleaned_data['username'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
            )

            profile.save()

            return redirect('show catalogue')
    else:
        form = CreateProfileForm()

    context = {
        'form': form,
    }

    return render(request, 'profile/create-profile.html', context)

def profile_details(request):
    profile = get_profile()
    plants_count = len(Plant.objects.all())

    context = {
        'profile': profile,
        'plants_count': plants_count,
    }

    return render(request, 'profile/profile-details.html', context)


def edit_profile(request):
    profile = get_profile()

    if request.method == 'POST':
        form = EditProfileForm(request.POST)
        if form.is_valid():
            profile.username = form.cleaned_data['username']
            profile.first_name = form.cleaned_data['first_name']
            profile.last_name = form.cleaned_data['last_name']
            profile.profile_picture = form.cleaned_data['profile_picture']
            profile.save()

            return redirect('profile details')
    else:
        form = EditProfileForm(initial={
            'username': profile.username,
            'first_name': profile.first_name,
            'last_name': profile.last_name,
            'profile_picture': profile.profile_picture
        })

    context = {
        'profile': profile,
        'form': form,
    }

    return render(request, 'profile/edit-profile.html', context)


def delete_profile(request):
    profile = get_profile()

    if request.method == 'POST':
        profile.delete()
        return redirect('show index')
    else:
        form = DeleteProfileForm(initial={
            'username': profile.username,
            'first_name': profile.first_name,
            'last_name': profile.last_name,
            'profile_picture': profile.profile_picture
        })

    context = {
        'form': form,
    }

    return render(request, 'profile/delete-profile.html', context)


def show_catalogue(request):
    profile = get_profile()
    plants = Plant.objects.all()

    plants_created = True if plants else False

    context = {
        'profile': profile,
        'plants_created': plants_created,
        'plants': plants,
    }

    return render(request, 'plants/catalogue.html', context)


def create_plant(request):
    if request.method == 'POST':
        form = CreatePlantForm(request.POST)
        if form.is_valid():
            plant = Plant(
                type=form.cleaned_data['type'],
                name=form.cleaned_data['name'],
                image_url=form.cleaned_data['image_url'],
                description=form.cleaned_data['description'],
                price=form.cleaned_data['price'],
            )

            plant.save()

            return redirect('show catalogue')
    else:
        form = CreatePlantForm()

    context = {
        'form': form,
    }

    return render(request, 'plants/create-plant.html', context)


def plant_details(request, pk):
    plant = get_object_or_404(Plant, pk=pk)

    context = {
        'plant': plant,
    }

    return render(request, 'plants/plant-details.html', context)


def edit_plant(request, pk):
    plant = get_object_or_404(Plant, pk=pk)

    if request.method == 'POST':
        form = EditPlantForm(request.POST)
        if form.is_valid():
            plant.type = form.cleaned_data['type']
            plant.name = form.cleaned_data['name']
            plant.image_url = form.cleaned_data['image_url']
            plant.description = form.cleaned_data['description']
            plant.price = form.cleaned_data['price']
            plant.save()

            return redirect('show catalogue')
    else:
        form = EditPlantForm(initial={
            'type': plant.type,
            'name': plant.name,
            'image_url': plant.image_url,
            'description': plant.description,
            'price': plant.price,
        })

    context = {
        'plant': plant,
        'form': form,
    }

    return render(request, 'plants/edit-plant.html', context)


def delete_plant(request, pk):
    plant = get_object_or_404(Plant, pk=pk)

    if request.method == 'POST':
        plant.delete()
        return redirect('show catalogue')
    else:
        form = DeletePlantForm(initial={
            'type': plant.type,
            'name': plant.name,
            'image_url': plant.image_url,
            'description': plant.description,
            'price': plant.price,
        })

    context = {
        'plant': plant,
        'form': form,
    }

    return render(request, 'plants/delete-plant.html', context)
