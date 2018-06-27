from django.conf.urls import url

from rest_framework.authtoken import views as rest_framework_views
from django.conf.urls import url
from rest_framework import routers
from api_inst.views import person_views, course_views, institution_views, subject_views, group_views, absence_views

router = routers.DefaultRouter()

urlpatterns = [
    url(r'^auth/$', rest_framework_views.obtain_auth_token, name='obtain_auth_token'),
    url(r'^course/', course_views.CourseAPI.as_view(), name='course_views'),
    url(r'^group/', group_views.GroupAPI.as_view(), name='group_views'),
    url(r'^institution/', institution_views.InstitutionAPI.as_view(), name='institution_views'),
    url(r'^person/', person_views.PersonAPI.as_view(), name='person_views'),
    url(r'^subject/', subject_views.SubjectAPI.as_view(), name='subject_views'),
    url(r'^absence/', absence_views.get_absences, name='get_absences_view'),
]
