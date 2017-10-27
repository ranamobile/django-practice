from django.conf.urls import url

from bingo_master import views


urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^list/$', views.list, name="list"),
    url(r'^game/$', views.game, name="game"),
    url(r'^history/$', views.history, name="history"),
]
