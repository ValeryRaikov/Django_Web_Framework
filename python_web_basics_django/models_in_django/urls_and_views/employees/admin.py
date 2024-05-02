from django.contrib import admin

from urls_and_views.employees.models import Employee


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'job_title', 'company',]
