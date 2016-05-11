from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from url_rest import views

urlpatterns = [
    url(r'^$', views.api_root),
    url(r'^url/$',
        views.UrlShortList.as_view(),
        name='url-list'),
    url(r'^url/(?P<pk>[0-9]+)/$',
        views.UrlShortDetail.as_view(),
        name='url-detail'),
    url(r'^url/(?P<pk>[0-9]+)/go/$',
        views.UrlShortGo.as_view(),
        name='url-go'),
]

urlpatterns = format_suffix_patterns(urlpatterns)