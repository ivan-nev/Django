from django.contrib import admin
from .models import Sensor, Measurement

admin.site.register(Sensor)


@admin.register(Measurement)
class MesurementAdmin(admin.ModelAdmin):
    list_display = ['sensor','temperature', 'created_at']

# Register your models here.
