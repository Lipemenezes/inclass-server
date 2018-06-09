from django.conf.urls import url

from rest_framework.authtoken import views as rest_framework_views
from django.conf.urls import url, include
from rest_framework import routers
from api_mobile import views

router = routers.DefaultRouter()


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^auth/$', views.obtain_auth_token, name='obtain_auth_token'),
    url(r'get-student-data', views.get_student_data, name='get_student_data'),
    url(r'get-professor-data', views.get_professor_data, name='get_professor_data'),
    url(r'get-admin-data', views.get_admin_data, name='get_admin_data'),
    url(r'get-absences-for-lecture', views.get_absences_for_lecture, name='get_absences_for_lecture'),
]
