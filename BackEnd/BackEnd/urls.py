
from django.conf.urls import url, include
from django.contrib import admin

from Data.views import PostLogin
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login$',PostLogin),
    url(r'^data/', include('Data.urls')),
    url(r'^', include('Web.urls')),

]