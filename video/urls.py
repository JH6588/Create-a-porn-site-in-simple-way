from django.conf.urls import url
from . import views

urlpatterns = [
url(r'^$' ,views.index ,name = 'index'),
    url(r'^page/(?P<page>[0-9]+)/$',views.show,name='show'),
    url(r'^video/(?P<vid>[0-9]+)/$' ,views.play ,name = 'play')

]