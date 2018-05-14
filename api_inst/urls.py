from django.conf.urls import url

from rest_framework.authtoken import views as rest_framework_views
from django.conf.urls import url, include
from rest_framework import routers
from api_inst import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^auth/$', rest_framework_views.obtain_auth_token, name='obtain_auth_token'),
]
