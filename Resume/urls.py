from django.conf.urls import url, include
from django.urls import path
from django.contrib import admin

urlpatterns = [
    path(r'', include('main.urls')),
    path(r'proj', include('projects.urls')),
    url(r'^admin/', admin.site.urls),
]
