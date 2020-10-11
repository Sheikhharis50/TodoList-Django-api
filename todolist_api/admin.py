from django.contrib import admin
from .models import *
from django.contrib.admin import AdminSite


class TodoModelAdmin(admin.ModelAdmin):
    list_display = [f.name for f in todo._meta.fields]


admin.site.register(todo, TodoModelAdmin)


class PingModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'state']
    list_editable = ('state',)


admin.site.register(ping, PingModelAdmin)
