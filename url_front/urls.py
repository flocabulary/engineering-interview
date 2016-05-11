from django.conf.urls import url
from url_front import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^(?P<short_url>[0-9a-zA-Z]+)/$', views.go_short_url),
]