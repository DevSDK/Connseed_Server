from collections import OrderedDict

from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db import models


#temperature
#humidity
#lux(밝기)
#ppm(공기오염)
#wtr(토양수분)

#int wtr;
#float ppm;
#float tmp;
#float hum;
#uint16_t lux;
from rest_framework import serializers



class LoRaDevice(models.Model):
    FK_User = models.ForeignKey(User)
    EUI = models.TextField(max_length=255)
    Battery = models.IntegerField()
    Nickname = models.CharField(max_length=255)

class LoRaData(models.Model):
    FK_Device = models.ForeignKey(LoRaDevice)
    Temperature = models.FloatField()
    Humidity = models.FloatField()
    Ppm = models.FloatField()
    Wtr = models.IntegerField()
    Lux = models.IntegerField()
    Date = models.DateTimeField(auto_now=True)

class LoRaStatisticalData_Day(models.Model):
    FK_Device = models.ForeignKey(LoRaDevice)
    Temperature = models.FloatField()
    Humidity = models.FloatField()
    Ppm = models.FloatField()
    Wtr = models.IntegerField()
    Lux = models.IntegerField()
    Date = models.DateTimeField(auto_now=True)

class LoRaStatisticalData_Week(models.Model):
    FK_Device = models.ForeignKey(LoRaDevice)
    Temperature = models.FloatField()
    Humidity = models.FloatField()
    Ppm = models.FloatField()
    Wtr = models.IntegerField()
    Lux = models.IntegerField()
    Date = models.DateTimeField(auto_now=True)

class LoRaStatisticalData_Month(models.Model):
    FK_Device = models.ForeignKey(LoRaDevice)
    Temperature = models.FloatField()
    Humidity = models.FloatField()
    Ppm = models.FloatField()
    Wtr = models.IntegerField()
    Lux = models.IntegerField()
    Date = models.DateTimeField(auto_now=True)

class LoRaRawSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoRaData
        fields = ('Temperature', 'Humidity','Ppm', 'Wtr', 'Lux','Date')


class LoRaDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = LoRaStatisticalData_Day
        fields = ('Temperature', 'Humidity','Ppm', 'Wtr', 'Lux','Date')

class LoRaWeekSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoRaStatisticalData_Week
        fields = ('Temperature', 'Humidity','Ppm', 'Wtr', 'Lux','Date')

class LoRaMonthSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoRaStatisticalData_Month
        fields = ('Temperature', 'Humidity','Ppm', 'Wtr', 'Lux','Date')


class LoRaDeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoRaDevice
        fields = ('id', 'EUI','Battery', 'Nickname')
