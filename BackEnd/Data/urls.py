from django.conf.urls import url, include
from django.contrib import admin

from Data.views import PostRawData, GetDeviceList, GetAllData, GetCurrentData, GetDateData

urlpatterns = [

    url('^getalldata$', GetAllData),
    url('^getcurrentdata$', GetCurrentData),
    url('^getdatedata$', GetDateData),
    url('^postrawdata$', PostRawData),
    url('^devicelist$', GetDeviceList),
]