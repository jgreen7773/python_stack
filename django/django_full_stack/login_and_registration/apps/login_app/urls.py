from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'^$', views.wall),
    url(r'^$', views.index),
    url(r'^success$', views.success),
]