from django.urls import path

from urls_and_views.employees.views import home, department, more, bad_request, go_to_home, html, html_with_css

urlpatterns = [
    path('', home),
    path('department/', department),
    path('<int:id>/', more),
    path('go-to-home/', go_to_home),
    path('html/', html, name='html'),
    path('page/', html_with_css, name='styled html'),
]
