from django.urls import path

from cbv_demo.main.views import TodoCreateView, IndexView, TodoListView, TodoDetailsView, TodoUpdateView, TodoDeleteView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('list-todos/', TodoListView.as_view(), name='list todos'),
    path('list-todos/<int:pk>/', TodoDetailsView.as_view(), name='todo details'),
    path('create/', TodoCreateView.as_view(), name='create'),
    path('update/<int:pk>', TodoUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', TodoDeleteView.as_view(), name='delete'),
]
