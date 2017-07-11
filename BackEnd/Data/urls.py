from django.conf.urls import url, include
from django.contrib import admin

from Data.views import GetRawData, PostRawData

urlpatterns = [

    url('^GetRawData$', GetRawData),
    url('^PostRawData$', PostRawData),

]