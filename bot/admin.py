from django.contrib import admin

from .models import Task, Setting


admin.site.register(Task)
admin.site.register(Setting)
