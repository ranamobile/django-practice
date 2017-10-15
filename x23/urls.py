from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin


urlpatterns = [
    url(r'^/?$', include("x24.urls")),
    url(r'^admin/', admin.site.urls),
    url(r'^bingo/', include("bingo_master.urls")),
]
