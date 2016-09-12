from django.conf.urls import url
from . import views

app_name = 'contact'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9a-zA-Z]+)/$', views.DetailView.as_view(), name='detail'),
]
