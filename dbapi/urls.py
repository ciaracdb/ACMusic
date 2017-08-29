from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    url(r'^playlists/$', views.PlaylistsListAPIView.as_view()),
    url(r'^playlists/(?P<pk>[0-9]+)$', views.PlaylistsDetailAPIView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)