from django.conf.urls import include, url

from django.contrib import admin
from rest_framework import routers

from dbapi import views

admin.autodiscover()


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    url(r'^', include('mainsite.urls')),
    url(r'^dbapi/', include('dbapi.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
