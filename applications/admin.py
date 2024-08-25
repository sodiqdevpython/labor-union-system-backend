from django.contrib import admin
from .models import Application

@admin.register(Application)
class AdminApplication(admin.ModelAdmin):
    list_display = ['user', 'title', 'status']
    list_filter = ['status']
    search_fields = ['user', 'title', 'body']