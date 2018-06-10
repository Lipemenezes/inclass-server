import json

from django.http import JsonResponse
from rest_framework.decorators import api_view

from inclass_server.models import Lecture, Absence, Dispute


@api_view(http_method_names=['GET'])
def get_professor_data(request):
    a = 'teste'
    return JsonResponse({'id': request.GET.get('professor_id')})


@api_view(http_method_names=['GET'])
def get_lecture(request):
    date = request.POST['date']
    lecture = Lecture.objects.filter(
        instructor_id=request.user.person.pk,
        group_id=request.POST['group_id'],
        date=date
    ).first()

    students_data = list()
    if lecture:
        absences = Absence.objects.filter(lecture=lecture)
        for absence in absences:
            students_data.append({
                'student_name': '{} {}'.format(absence.student.user.first_name, absence.student.user.last_name),
                'student_id': absence.student.pk,
                'absence_number': absence.absence_number
            })

    return JsonResponse({
        'students_absences': students_data,
        'workload': lecture.workload
    })


@api_view(http_method_names=['POST'])
def set_lecture(request):
    date = request.POST['date']
    lecture = Lecture.update_or_create(
        instructor_id=request.user.person.pk,
        group_id=request.POST['group_id'],
        workload=request.POST['workload'],
        date=date
    )

    for student_absence in json.loads(request.POST['students_absences']):
        absence_number = int(student_absence['absence_number'])
        if absence_number > 0:
            Absence.update_or_create(
                lecture_id=lecture.id,
                student_id=student_absence['student_id'],
                absence_number=lecture.workload - absence_number
            )

    return JsonResponse({'status': "success"})


@api_view(http_method_names=['GET'])
def get_open_disputes(request):
    open_disputes = Dispute.objects.filter(absence__lecture__instructor=request.user.person, status=Dispute.WAITING)
    dispute_list = list()
    for dispute in open_disputes:
        dispute_list.append({
            'student_name': '{} {}'
                .format(dispute.absence.student.user.first_name, dispute.absence.student.user.last_name),
            'subject_name': dispute.absence.lecture.group.subject.name,
            'date': dispute.absence.lecture.date,
            'absence_number': dispute.absence.absence_number,
            'message': dispute.message,
            'status': dispute.status
        })

    return JsonResponse({'status': "success"})


@api_view(http_method_names=['POST'])
def close_dispute(request):
    is_approved = request.POST['approved']
    dispute = Dispute.objects.get(pk=request.POST['dispute_id'])
    if is_approved:
        dispute.approve(request.POST['final_absence_number'])
    else:
        dispute.refuse()

    return JsonResponse({'status': "success"})