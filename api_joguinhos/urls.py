from django.conf.urls import url
from rest_framework import routers

from api_joguinhos import views

router = routers.DefaultRouter()

urlpatterns = [
    url(r'^get-joguinhos/$', views.joguinhos, name='joguinhos'),
    url(r'^register/', views.register, name='register'),
    url(r'^auth/', views.authenticate_user, name='authenticate'),
]
