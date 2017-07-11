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

from Data.models import LoLaData, LoLaDevice, LoLaRawSerializer, LoLaDeviceSerializer


@csrf_exempt
def PostRawData(request):
    try:
        if request.method == 'GET':
            return HttpResponse("Invalid Method")
        Device_ID = request.POST.get("device")
        Wtr = request.POST.get("wtr")
        Ppm = request.POST.get('ppm')
        Tmp = request.POST.get('tmp')
        Hum = request.POST.get('hum')
        Lux = request.POST.get('lux')
        if Device_ID is None or Wtr is None or Ppm is None or Tmp is None or Hum is None or Lux is None:
            return HttpResponse("Less Parameter")
        Device = LoLaDevice.objects.get(pk = Device_ID)
        if Device is None:
            return HttpResponse("Invalid Device", status=501)

        query = LoLaData(FK_Device=Device, Temperature=Tmp, Humidity=Hum, Ppm = Ppm, Wtr = Wtr, Lux=Lux)
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
            return HttpResponse("Invalid Method")
        device = request.GET['device']
        data = LoLaData.objects.filter(FK_Device=device)

        serializer = LoLaRawSerializer(data, many=True)

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

        data = LoLaDevice.objects.filter(FK_User=request.user)
        serializer = LoLaDeviceSerializer(data, many=True)
        return Response(serializer.data, content_type=u"application/json; charset=utf-8")
    except Exception as e:
        HttpResponse(e, status=501)



