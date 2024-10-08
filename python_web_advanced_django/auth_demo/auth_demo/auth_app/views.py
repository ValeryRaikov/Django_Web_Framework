from django.contrib.auth import forms, get_user_model, login
from django.contrib.auth.views import LoginView, LogoutView
from django.forms import ModelForm
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from auth_demo.auth_app.models import Profile


def index(request):
    return render(request, 'main/index.html')


UserModel = get_user_model()


class UserRegistrationForm(forms.UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('email',)

    def save(self, commit=True):
        user = super().save(commit=commit)

        profile = Profile(
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            user=user,
        )

        if commit:
            profile.save()

        return user


class ProfileCreateForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ('user',)


class UserRegistrationView(CreateView):
    # form_class = forms.UserCreationForm
    form_class = UserRegistrationForm
    template_name = 'auth/register.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile_form'] = ProfileCreateForm()
        return context

    def form_valid(self, form):
        result = super().form_valid(form)

        # profile = Profile(
        #     first_name=form.cleaned_data['first_name'],
        #     last_name=form.cleaned_data['last_name'],
        #     user=self.object,
        # )
        # profile.save()

        login(self.request, self.object)

        return result


class UserLoginView(LoginView):
    template_name = 'auth/login.html'

    def get_success_url(self):
        next = self.request.GET.get('next', None)

        return next if next else reverse_lazy('home')


class UserLogoutView(LogoutView):
    def get_success_url(self):
        return reverse_lazy('home')
