# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import JsonResponse

# Create your views here.
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response

from inclass_server.models import Person, Institution, Group, Absence


@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def obtain_auth_token(request, *args, **kwargs):
    user = authenticate(username=request.POST['username'], password=request.POST['password'])
    if user:
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'is_student': user.has_perm('inclass_server.is_student'),
            'is_professor': user.has_perm('inclass_server.is_professor'),
            'is_admin': user.has_perm('inclass_server.is_admin'),
            'user_id': user.pk,
            'name': '{} {}'.format(user.first_name, user.last_name),
            'email': user.email,
            'matricula': user.person.register,
            'institution': Institution.objects.first().name,

        })
    else:
        return Response({
            'error': 'invalid credentials'
        })


@api_view(http_method_names=['GET'])
def get_student_data(request):
    person = request.user.person
    groups = Group.objects.filter(students=person)
    groups_list = list()
    for group in groups:
        instructors_list = []
        for instructor in group.instructors:
            instructors_list.append({
                'id': instructor.pk,
                'name': instructor.name,
            })

        groups_list.append({
            'group_id': group.pk,
            'name': group.subject.name,
            'workload': group.subject.workload,
            'days_of_the_week': '',
            'instructors': instructors_list,
            'number_of_absences': Absence.get_total(person, group)
        })
    return JsonResponse(groups_list)


@api_view(http_method_names=['GET'])
def get_professor_data(request):
    a = 'teste'
    return JsonResponse({'id': request.GET.get('professor_id')})


@api_view(http_method_names=['GET'])
def get_admin_data(request):
    a = 'teste'
    return JsonResponse({'id': request.GET.get('professor_id')})


@api_view(http_method_names=['GET'])
def get_absences_for_lecture(request):
    group_id = request.GET['group_id']
    absences = Absence.objects.filter(student__id=request.user.person.id, lecture__group__id=group_id)
    absences_list = list()
    for absence in absences:
        absences_list.append({
            'absence_id': absence.pk,
            'subject': absence.lecture.group.subject.name,
            'instructor': '{} {}'
                .format(absence.lecture.instructor.user.first_name, absence.lecture.instructor.user.last_name),
            'absence_number': absence.absence_number,
            'date': absence.lecture.date,
            'has_dispute': absence.has_dispute()
        })

    return JsonResponse(absences_list)
