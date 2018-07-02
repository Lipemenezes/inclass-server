from django.conf.urls import url
from rest_framework import routers

from api_frutinha import views

router = routers.DefaultRouter()

urlpatterns = [
    url(r'^get-fruits/$', views.fruits, name='fruits'),
    url(r'^register/', views.register, name='register'),
    url(r'^auth/', views.authenticate, name='authenticate'),
]
