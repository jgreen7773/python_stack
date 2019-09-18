from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^shows$', views.AllShows),
    url(r'^shows/new$', views.AddNewShow),
    url(r'^shows/(?P<edit_show>\d+)/edit$', views.EditShow2),
    url(r'^shows/(?P<id>\d+)$', views.TVShow2),
    url(r'^shows/(?P<id>\d+)/destroy$', views.Destroy),
]