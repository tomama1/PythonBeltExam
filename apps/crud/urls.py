from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'register$', views.register),
    url(r'login$', views.login),
    url(r'destination/(?P<id>\d+)$', views.displaytrip),
    url(r'travels$', views.travels),
    url(r'travels/join/(?P<id>\d+)$', views.traveljoin),
    url(r'travels/addprocess$', views.addprocess),
    url(r'travels/add$', views.display_addtrip),
    url(r'logout$', views.logout),
]
