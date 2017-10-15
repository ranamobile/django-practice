from django.conf.urls import url

from x24 import views


urlpatterns = [
    url(r'^$', views.index),
]
