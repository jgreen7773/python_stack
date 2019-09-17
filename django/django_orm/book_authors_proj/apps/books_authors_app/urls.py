from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.addbook),
    url(r'^authors$', views.addauthor),
    url(r'^books/(?P<book_id>\d+)$', views.displaybook),
    url(r'^authors/(?P<author_id>\d+)$', views.displayauthor),
]