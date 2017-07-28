from django.conf.urls import url
#from .forms import EventForm1, EventForm2
from . import views

urlpatterns = [
    url(r'^$', views.EventWizard.as_view(), name='index'),
    url(r'^result/(?P<pk>\d+)/$', views.result, name='result'),
    url(r'^send/(?P<pk>\d+)/$', views.send, name='send'),
]

