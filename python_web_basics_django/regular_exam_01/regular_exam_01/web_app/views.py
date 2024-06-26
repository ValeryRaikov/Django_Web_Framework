from django.shortcuts import render, redirect

from regular_exam_01.web_app.models import Profile, Album
from regular_exam_01.web_app.forms import (CreateProfileForm, EditProfileForm, DeleteProfileForm, AddAlbumForm,
                                           EditAlbumForm, DeleteAlbumForm)


# Only one profile!
def get_profile():
    profiles = Profile.objects.all()

    if profiles:
        return profiles[0]

    return None


def show_home(request):
    profile = get_profile()

    if not profile:
        return redirect('profile create')

    albums = Album.objects.all()

    context = {
        'profile': profile,
        'albums': albums,
    }

    return render(request, 'web_app/home-with-profile.html', context)


def album_add(request):
    if request.method == 'POST':
        form = AddAlbumForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect('show home')
    else:
        form = AddAlbumForm()

    context = {
        'form': form,
    }

    return render(request, 'album/add-album.html', context)


def album_details(request, pk):
    album = Album.objects.get(pk=pk)

    context = {
        'album': album,
    }

    return render(request, 'album/album-details.html', context)


def album_edit(request, pk):
    album = Album.objects.get(pk=pk)

    if request.method == 'POST':
        form = EditAlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()

        return redirect('show home')
    else:
        form = AddAlbumForm(instance=album)

    context = {
        'album': album,
        'form': form,
    }

    return render(request, 'album/edit-album.html', context)


def album_delete(request, pk):
    album = Album.objects.get(pk=pk)

    if request.method == 'POST':
        form = DeleteAlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()

        return redirect('show home')
    else:
        form = DeleteAlbumForm(instance=album)

    context = {
        'album': album,
        'form': form,
    }

    return render(request, 'album/delete-album.html', context)


def profile_details(request):
    profile = get_profile()
    albums = Album.objects.all()

    context = {
        'profile': profile,
        'albums_count': len(albums),
    }

    return render(request, 'profile/profile-details.html', context)


def profile_create(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            return redirect('show home')
    else:
        form = CreateProfileForm()

    context = {
        'form': form,
    }

    return render(request, 'web_app/home-no-profile.html', context)


def profile_edit(request):
    profile = get_profile()

    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()

            return redirect('show home')
    else:
        form = EditProfileForm(instance=profile)

    context = {
        'form': form,
    }

    return render(request, 'profile/profile_edit.html', context)


def profile_delete(request):
    profile = get_profile()

    if request.method == 'POST':
        form = DeleteProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()

            return redirect('show home')
    else:
        form = DeleteProfileForm(instance=profile)

    context = {
        'form': form,
    }

    return render(request, 'profile/profile-delete.html', context)
