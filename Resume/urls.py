from django.conf.urls import url, include
from django.urls import path
from django.contrib import admin

urlpatterns = [
    path(r'', include('main.urls')),
    url(r'^admin/', admin.site.urls),
]
