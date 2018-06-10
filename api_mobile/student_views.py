# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import JsonResponse
from rest_framework.decorators import api_view
from inclass_server.models import Group, Absence, Dispute


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


@api_view(http_method_names=['POST'])
def open_dispute(request):
    absence = Absence.objects.get(id=request.POST['absence_id'])
    Dispute(
        absence=absence,
        message=request.POST['message'],
        initial_absence_number=absence.absence_number,
        final_absence_number=absence.absence_number,
        is_deleted=False,
        status=Dispute.WAITING
    ).save()
    return JsonResponse({'status': "success"})


@api_view(http_method_names=['GET'])
def get_disputes(request):
    disputes = Dispute.objects.filter(absence__student=request.user.person)
    disputes_list = list()
    for dispute in disputes:
        disputes_list.append({
            'dispute_id': dispute.pk,
            'date': dispute.absence.lecture.date,
            'initial_absence_number': dispute.initial_absence_number,
            'final_absence_number': dispute.final_absence_number,
            'professor': dispute.absence.lecture.instructor,
            'status': dispute.status,
            'message': dispute.message
        })
    return JsonResponse(disputes_list)
