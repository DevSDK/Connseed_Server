
from django.conf.urls import url, include
from django.contrib import admin

from Web.views import *

urlpatterns = [

    url(r'', MainPage),
]