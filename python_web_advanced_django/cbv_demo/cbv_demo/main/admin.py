from django.contrib import admin

from cbv_demo.main.models import Todo


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    pass
