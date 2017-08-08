from django.conf.urls import url

from . import  views



urlpatterns = [
    url(r'^users/manage$', views.user_manage),
    url(r'^register/', views.register),
    url(r'^user/(?P<uid>[0-9]+)/$', views.user),
    url(r'^user/center/$', views.user_center),
    url(r'^group/(?P<gid>[0-9]+)/$', views.group),
    ]