from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^playlists_list$', views.PlaylistsList.as_view()),
]