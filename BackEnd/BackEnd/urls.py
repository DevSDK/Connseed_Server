
from django.conf.urls import url, include
from django.contrib import admin

from Data.views import PostLogin
from Web.views import Account, Analysis, Device, Monitoring

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^Login$',PostLogin),
    url(r'^Data/', include('Data.urls')),
    url(r'^', include('Web.urls')),

]