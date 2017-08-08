"""opssystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from . import  views
from cmdb import  urls as cmdb_urls
from usercenter import  urls  as usercenter_urls
from codedeploy import  urls as codedeploy_urls
from taskmanager import  urls as taskmanager_urls
from appdeploy import  urls as appdeploy_urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.index,name="index"),
    url(r"^asset/",include(cmdb_urls)),
    url(r"^uc/",include(usercenter_urls)),
    url(r"^codedeploy/", include(codedeploy_urls)),
    url(r"^task/",include(taskmanager_urls)),
    url(r"^appdeploy/",include(appdeploy_urls)),
    url(r'^login/', views.login),
    url(r'^logout', views.logout),
    url(r'^config', views.config),
    url(r'^noperm', views.noperm),
    url(r'^config', views.config),

]
