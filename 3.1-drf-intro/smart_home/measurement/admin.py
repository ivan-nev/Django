from django.contrib import admin
from .models import Sensor, Measurement

@admin.register(Sensor)
class SensoAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'foto']


@admin.register(Measurement)
class MesurementAdmin(admin.ModelAdmin):
    list_display = ['sensor','temperature', 'created_at']

# Register your models here.
