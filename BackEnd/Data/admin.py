from django.contrib import admin

# Register your models here.
from Data.models import LoRaDevice, LoRaData, LoRaStatisticalData_Day, LoRaStatisticalData_Week, \
    LoRaStatisticalData_Month

admin.site.register(LoRaDevice)
admin.site.register(LoRaData)

admin.site.register(LoRaStatisticalData_Day)
admin.site.register(LoRaStatisticalData_Week)
admin.site.register(LoRaStatisticalData_Month)
