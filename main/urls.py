from django.conf.urls import include
from django.urls import path

from . import views

app_name = 'main'

urlpatterns = [
    path(r'', views.home, name='home'),
    path(r'about', views.about, name='about'),
    path(r'contact', views.contact, name='contect'),
]