from django.conf.urls import url

from . import  views
urlpatterns = [
    url(r'^cron_add',views.cron_add,name="cron_add"),
    url(r'^cron_list',views.cron_list,name="cron_list"),
    url(r'^cron_config',views.cron_config,name="cron_config"),
    url(r'^cron_log',views.cron_log,name="cron_log"),
    url(r'^cron_mod/(?P<cid>[0-9]+)/$',views.cron_mod,name="cron_mod"),

    #url(r'test',views.test,name='test'),

]