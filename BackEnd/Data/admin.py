from django.contrib import admin

# Register your models here.
from Data.models import LoRaDevice, LoRaData

admin.site.register(LoRaDevice)
admin.site.register(LoRaData)