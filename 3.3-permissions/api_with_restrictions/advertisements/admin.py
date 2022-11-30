from django.contrib import admin
from advertisements.models import Advertisement


@admin.register(Advertisement)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['creator', 'title', 'description', 'status']
# Register your models here.
