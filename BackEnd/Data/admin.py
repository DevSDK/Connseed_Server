from django.contrib import admin

# Register your models here.
from Data.models import LoLaDevice, LoLaData

admin.site.register(LoLaDevice)
admin.site.register(LoLaData)