from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^login$', views.login),
    url(r'^signup$', views.signup),
    url(r'^processlogin$', views.processlogin),
    url(r'^processregistration$', views.processregistration),
    url(r'^wall$', views.wall),
    url(r'^logout$', views.logout),
    url(r'^delete$', views.delete),
    url(r'^processmessage$', views.processmessage),
    url(r'^processcomment$', views.processcomment),
    url(r'^processreply$', views.processreply),
]