from django.conf.urls import url, include
from django.contrib import admin

from Data.views import GetRawData, PostRawData, GetDeviceList

urlpatterns = [

    url('^GetRawData$', GetRawData),
    url('^PostRawData$', PostRawData),
    url('^DeviceList$', GetDeviceList),
]