from django.conf.urls import url
from . import views

app_name = "userauth"
urlpatterns = [
    url(r'^login/', views.user_login, name='login'),
    url(r'^dologin/', views.dologin, name='dologin'),
	url(r'^logout/', views.user_logout, name='logout'),
]
