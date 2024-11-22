from django.contrib import admin
from .models import EnvironmentalData, Crop
from unfold.admin import ModelAdmin as UnfoldModelAdmin
from unfold.admin import ModelAdmin


@admin.register(EnvironmentalData)
class EnvironmentalDataAdmin(UnfoldModelAdmin):
    list_display = ('timestamp', 'soil_moisture', 'temperature', 'humidity')

@admin.register(Crop)
class CropAdmin(UnfoldModelAdmin):
    list_display = ('name', 'ideal_temperature', 'ideal_soil_moisture')
