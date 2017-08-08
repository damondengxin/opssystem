from django.conf.urls import url

from . import  views
urlpatterns = [
    url(r'^assets_config',views.assets_config,name='assets_config'),
    url(r'^assets_add',views.assets_add,name="assets_add"),
    url(r'^assets_list',views.assets_list,name="assets_list"),
    url(r'^assets_mod/(?P<aid>[0-9]+)/$',views.assets_modf,name="assets_modf"),
    url(r'^assets_view/(?P<aid>[0-9]+)/$',views.assets_view,name="assets_views"),
    url(r'^assets_facts',views.assets_facts,name='assets_facts'),
    url(r'^assets_log/',views.assets_log,name="assets_log"),

    #url(r'test',views.test,name='test'),

]