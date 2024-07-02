from django.urls import path

from working_with_js.test_app.views import show_index, show_departments, show_people, register_person, show_all_simple

urlpatterns = [
    path('', show_index, name='show index'),
    path('departments/', show_departments, name='show departments'),
    path('people/', show_people, name='show people'),
    path('register/', register_person, name='register person'),
    path('show-all/', show_all_simple, name='show all'),
]
