from django.shortcuts import render
from django.views import generic as views
from django.urls import reverse_lazy
from .models import Profile, Account


class ProfileCreateView(views.CreateView):
    model = Profile
    fields = '__all__'
    template_name = 'profiles/create.html'

    def get_success_url(self):
        return reverse_lazy('profile details', kwargs={'pk': self.object.pk})


class ProfileListView(views.ListView):
    model = Profile
    template_name = 'profiles/list.html'

    def get_context_data(self, *args, **kwargs):
        context =  super().get_context_data(*args, *kwargs)

        if self.request.user.is_authenticated:
            context['user'] = self.request.user.username
        else:
            context['user'] = 'No user'


        return context
class ProfileDetailsView(views.DetailView):
    model = Profile
    template_name = 'profiles/details'
