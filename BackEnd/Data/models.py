from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db import models


#temperature
#humidity
#lux(밝기)
#ppm(공기오염)
#wtr(토양수분)

#nt wtr;
#float ppm;
#float tmp;
#float hum;
#uint16_t lux;

class LoLaDevice(models.Model):
    FK_User = models.ForeignKey(User)
    EUI = models.TextField(max_length=255)
    Nickname = models.CharField(max_length=255)




class LoLaData(models.Model):
    FK_Device = models.ForeignKey(LoLaDevice)
    Temperature = models.FloatField()
    Humidity = models.FloatField()
    Ppm = models.FloatField()
    Wtr = models.IntegerField()
    Lux = models.IntegerField()
