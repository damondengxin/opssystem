from django.conf.urls import url

from . import  views
urlpatterns = [
    url(r'^apps/$', views.apps_list,name="apps_list"),
    url(r'^apps/model/$', views.apps_model,name="apps_model"),
    url(r'^apps/run/$', views.ansible_run,name="ansible_run"),
    url(r'^apps/log/$', views.ansible_log,name="ansible_log"),
    url(r'^apps/log/(?P<model>[a-z]+)/(?P<id>[0-9]+)/$', views.ansible_log_view,name="ansible_log"),
    url(r'^apps/playbook/add/$', views.apps_add,name="ansible_add"),
    url(r'^apps/playbook/file/(?P<pid>[0-9]+)/$', views.apps_playbook_file,name="apps_playbook_file"),
    url(r'^apps/playbook/run/(?P<pid>[0-9]+)/$', views.apps_playbook_run,name="app_playbook_run"),
    url(r'^apps/playbook/modf/(?P<pid>[0-9]+)/$', views.apps_playbook_modf,name="app_playbook_modf"),

    #url(r'test',views.test,name='test'),

]