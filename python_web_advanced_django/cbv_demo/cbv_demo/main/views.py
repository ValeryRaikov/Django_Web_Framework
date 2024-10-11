from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Todo


class IndexView(TemplateView):
    template_name = 'main/index.html'


class TodoListView(ListView):
    model = Todo
    context_object_name = 'todos'
    template_name = 'main/list-todos.html'


class TodoDetailsView(DetailView):
    model = Todo
    template_name = 'main/todo-details.html'


class TodoCreateView(CreateView):
    model = Todo
    fields = '__all__'
    success_url = reverse_lazy('index')
    template_name = 'main/create.html'


class TodoUpdateView(UpdateView):
    model = Todo
    fields = '__all__'
    success_url = reverse_lazy('index')
    template_name = 'main/update.html'


class TodoDeleteView(DeleteView):
    model = Todo
    success_url = reverse_lazy('index')
    template_name = 'main/delete.html'
