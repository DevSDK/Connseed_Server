from django.contrib import auth
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
#nt wtr;
#float ppm;
#float tmp;
#float hum;
#uint16_t lux;
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from Data.models import LoRaData, LoRaDevice, LoRaRawSerializer, LoRaDeviceSerializer


@csrf_exempt
def PostRawData(request):
    try:
        if request.method == 'GET':
            return HttpResponse("Invalid Method")
        if not request.user.is_authenticated():
            return HttpResponse("Not Login", status=401)

        Device_ID = request.POST.get("device")
        Wtr = request.POST.get("wtr")
        Ppm = request.POST.get('ppm')
        Tmp = request.POST.get('tmp')
        Hum = request.POST.get('hum')
        Lux = request.POST.get('lux')
        if Device_ID is None or Wtr is None or Ppm is None or Tmp is None or Hum is None or Lux is None:
            return HttpResponse("Less Parameter")
        Device = LoRaDevice.objects.get(pk = Device_ID)
        if Device is None:
            return HttpResponse("Invalid Device", status=501)

        query = LoRaData(FK_Device=Device, Temperature=Tmp, Humidity=Hum, Ppm = Ppm, Wtr = Wtr, Lux=Lux)
        query.save()
        return HttpResponse("OK")
    except Exception as e:
        return HttpResponse(e, status=501)


def PostStatisticalData(request):
    pass
@api_view(['GET'])
@renderer_classes((JSONRenderer,))
def GetRawData(request):
    try:
        if request.method == 'POST':
            return HttpResponse("Invalid Method", status=400)
        device = request.GET.get('device')
        if device is None:
            return HttpResponse("require parameter : device id", status=400)

        data = LoRaData.objects.filter(FK_Device=device)

        serializer = LoRaRawSerializer(data, many=True)

        return Response(serializer.data)
    except Exception as e:
        HttpResponse(e, status=501)

def GetStatisticalData(request):
    pass


@api_view(['GET'])
@renderer_classes((JSONRenderer,))
def GetDeviceList(request):

    try:
        if request.method == 'POST':
            return HttpResponse('Invali method', status=400)
        if not request.user.is_authenticated():
            return HttpResponse('Not Login', status=401)

        data = LoRaDevice.objects.filter(FK_User=request.user)
        serializer = LoRaDeviceSerializer(data, many=True)
        return Response(serializer.data, content_type=u"application/json; charset=utf-8")
    except Exception as e:
        HttpResponse(e, status=501)



@csrf_exempt
def PostLogin(request):
    try:
        if request.method == 'GET':
            return HttpResponse("Invalid  GET Method",status=401)
        if request.method == 'POST':
            if request.user.is_authenticated():
                return HttpResponse("IsLogined",status=401)

            id = request.POST.get("id")
            pw = request.POST.get('pw')
            if id is None or pw is None:
                return HttpResponse("Parameter Denied",status=401)
            user = auth.authenticate(username=id, password=pw)
            if user is None:
                return HttpResponse("Login InValid",status=401)
            if user.is_active:
               auth.login(request, user)
            return HttpResponse('OK')
    except Exception as e:
        return HttpResponse(e, status=400)
