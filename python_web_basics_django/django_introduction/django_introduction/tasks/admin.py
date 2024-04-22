from django.contrib import admin

from django_introduction.tasks.models import Tasks


@admin.register(Tasks)
class TasksAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_filter = ['title']
    sortable_by = ['title']
