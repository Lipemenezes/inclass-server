from django.conf.urls import url, include
from rest_framework import routers
from api_mobile import views, student_views, professor_views

router = routers.DefaultRouter()


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^auth', views.obtain_auth_token, name='obtain_auth_token'),

    url(r'get-student-data', student_views.get_student_data, name='get_student_data'),
    url(r'get-absences-for-lecture', student_views.get_absences_for_lecture, name='get_absences_for_lecture'),
    url(r'open-dispute', student_views.open_dispute, name='open_dispute'),
    url(r'get-disputes', student_views.get_disputes, name='get_student_disputes'),

    url(r'get-professor-data', professor_views.get_professor_data, name='get_professor_data'),
    url(r'get-lecture', professor_views.get_lecture, name='get_lecture'),
    url(r'set-lecture', professor_views.set_lecture, name='set_lecture'),
    url(r'all-disputes-open', professor_views.get_open_disputes, name='get_open_disputes'),
    url(r'close-dispute', professor_views.close_dispute, name='close_dispute'),

    url(r'get-admin-data', views.get_admin_data, name='get_admin_data'),
]
