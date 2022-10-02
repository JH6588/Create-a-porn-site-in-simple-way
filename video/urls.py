from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^page/(?P<page>[0-9]+)/$', views.show, name='show'),
    re_path(r'^video/(?P<vid>[0-9]+)/$', views.play, name='play')
]
