from django.conf.urls import url
from . import views

app_name = "wxmanager"
urlpatterns = [
    url(r'^$', views.selectopening, name='selectopening'),
    url(r'^(?P<opening_id>[0-9]+)/$', views.checkin, name='checkin'),
    url(r'^(?P<opening_id>[0-9]+)/check$', views.check, name='check'),
]
