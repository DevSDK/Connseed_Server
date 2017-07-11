
from django.conf.urls import url, include
from django.contrib import admin

from Web.views import Account, Analysis, Device, Monitoring

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^account', Account),
    url(r'^analysis', Analysis),
    url(r'^device', Device),
    url(r'^monitoring', Monitoring),

    url(r'^Data/', include('Data.urls')),

    url(r'^$', include('Web.urls')),

]