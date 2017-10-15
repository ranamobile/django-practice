from django.conf.urls import url

from bingo_master import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'^list/$', views.list),
    url(r'^game/$', views.game),
    url(r'^history/$', views.history),
]
