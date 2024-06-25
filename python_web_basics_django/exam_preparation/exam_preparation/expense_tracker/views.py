from django.shortcuts import render, redirect
from exam_preparation.expense_tracker.models import Profile, Expense
from exam_preparation.expense_tracker.forms import (CreateProfileForm, EditProfileForm, DeleteProfileForm,
                                                    CreateExpenseForm, EditExpenseForm, DeleteExpenseForm)


def get_profile():
   all_profiles = Profile.objects.all()
   if all_profiles:
       return all_profiles[0]

   return None


def show_index(request):
    profile = get_profile()
    if not profile:
        return redirect('create profile')

    expenses = Expense.objects.all()
    left_budget = profile.budget - sum(e.price for e in expenses)

    context = {
        'profile': profile,
        'expenses': expenses,
        'left_budget': left_budget,
    }

    return render(request, 'home-no-profile.html', context)


def create_expense(request):
    if request.method == 'POST':
        form = CreateExpenseForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('show index')
    else:
        form = CreateExpenseForm()

    context = {
        'form': form,
    }

    return render(request, 'expense-create.html', context)


def edit_expense(request, pk):
    expense = Expense.objects.get(pk=pk)

    if request.method == 'POST':
        form = EditExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()

            return redirect('show index')
    else:
        form = EditExpenseForm(instance=expense)

    context = {
        'form': form,
    }

    return render(request, 'expense-edit.html', context)


def delete_expense(request, pk):
    expense = Expense.objects.get(pk=pk)

    if request.method == 'POST':
        form = DeleteExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()

            return redirect('show index')
    else:
        form = DeleteExpenseForm(instance=expense)

    context = {
        'form': form,
    }

    return render(request, 'expense-delete.html', context)


def show_profile(request):
    profile = get_profile()
    expenses = Expense.objects.all()

    left_budget = profile.budget - sum(e.price for e in expenses)

    context = {
        'profile': profile,
        'expenses_count': len(expenses),
        'left_budget': left_budget,
    }

    return render(request, 'profile.html', context)


def create_profile(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            return redirect('show index')
    else:
        form = CreateProfileForm()

    context = {
        'form': form,
        'no_profile': True,
    }

    return render(request, 'home-no-profile.html', context)


def edit_profile(request):
    profile = get_profile()

    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()

            return redirect('show index')
    else:
        form = EditProfileForm(instance=profile)

    context = {
        'form': form,
    }

    return render(request, 'profile-edit.html', context)


def delete_profile(request):
    profile = get_profile()

    if request.method == 'POST':
        form = DeleteProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()

            return redirect('show index')
    else:
        form = DeleteProfileForm(instance=profile)

    context = {
        'form': form,
    }

    return render(request, 'profile-delete.html', context)
