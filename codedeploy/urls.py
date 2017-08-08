from django.conf.urls import url

from . import  views
urlpatterns = [
    url(r'^deploy_add', views.deploy_add),
    url(r'^deploy_list', views.deploy_list),
    url(r'^deploy_log', views.deploy_log),
    url(r'^deploy_mod/(?P<pid>[0-9]+)/$', views.deploy_modf),
    url(r'^deploy_init/(?P<pid>[0-9]+)/$', views.deploy_init),
    url(r'^deploy_version/(?P<pid>[0-9]+)/$', views.deploy_version),
    url(r'^deploy_run/(?P<pid>[0-9]+)/$', views.deploy_run),
    url(r'^deploy_result/(?P<pid>[0-9]+)/$', views.deploy_result),
    url(r'^deploy_ask/(?P<pid>[0-9]+)/$', views.deploy_ask),
    url(r'^deploy_order/$', views.deploy_order),
    url(r'^deploy_order/status/(?P<pid>[0-9]+)/$', views.deploy_order_status),
    url(r'^deploy_order/rollback/(?P<pid>[0-9]+)/$', views.deploy_order_rollback),
    url(r'^deploy_manage/(?P<pid>[0-9]+)/$', views.deploy_manage),

    #url(r'test',views.test,name='test'),

]

