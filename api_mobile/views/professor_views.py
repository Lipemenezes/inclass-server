import json

from django.http import JsonResponse
from rest_framework.decorators import api_view
from datetime import datetime
from inclass_server.models import Lecture, Absence, Dispute, Group


@api_view(http_method_names=['GET'])
def get_professor_data(request):
    try:
        groups = Group.objects.filter(instructors=request.user.person) \
            .select_related('subject').select_related('course')

        courses_dict = dict()

        for group in groups:
            if not courses_dict.get(group.course.external_code):
                courses_dict[group.course.external_code] = {
                    'course_name': group.course.name,
                    'course_initials': group.course.initials,
                    'course_id': group.course.pk,
                    'groups': list()
                }

            courses_dict[group.course.external_code]['groups'].append({
                'days_of_the_week': group.get_days_of_the_week_string(),
                'semester': group.semester,
                'year': group.year,
                'day_period': group.day_period,
                'external_code': group.external_code,
                'group_id': group.pk,
                'subject_name': group.subject.name,
                'subject_id': group.subject.pk,
            })

        courses_list = list()
        for k, v in courses_dict.items():
            courses_list.append(v)

        return JsonResponse({'status': 'success', 'courses': courses_list})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=400)


@api_view(http_method_names=['GET'])
def get_lecture(request):
    try:
        date = datetime.strptime(request.GET['date'], '%Y-%m-%d')
        lecture = Lecture.objects.filter(
            instructor_id=request.user.person.pk,
            group_id=request.GET['group_id'],
            date=date
        ).first()

        if not lecture:
            group = Group.objects.filter(pk=request.GET['group_id']).first()
        else:
            group = lecture.group

        students_data = dict()
        for student in group.students.all().select_related('user'):
            students_data[student.pk] = {
                'student_name': student.get_full_name(),
                'student_id': student.pk,
                'absence_number': None
            }

        workload = None
        if lecture:
            absences = Absence.objects.filter(lecture=lecture).select_related('student')
            for absence in absences:
                if absence.student.pk in students_data:
                    students_data[absence.student.pk]['absence_number'] = absence.absence_number
            workload = lecture.workload

        students_list = list()
        for k, v in students_data.items():
            students_list.append(v)

        return JsonResponse({
            'students_absences': students_list,
            'workload': workload
        })

    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=400)


@api_view(http_method_names=['POST'])
def set_lecture(request):
    try:
        payload = json.loads(request.body)
        date = datetime.strptime(payload['date'], '%Y-%m-%d')

        lecture = Lecture.update_or_create(
            instructor_id=request.user.person.pk,
            group_id=payload['group_id'],
            workload=payload['workload'],
            date=date
        )

        try:
            students_absences = json.loads(payload['students_absences'])
        except:
            students_absences = payload['students_absences']

        for student_absence in students_absences:
            absence_number = student_absence.get('absence_number')
            Absence.update_or_create(
                lecture=lecture,
                student_id=student_absence['student_id'],
                absence_number=absence_number
            )

        return JsonResponse({'status': "success"})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=400)


@api_view(http_method_names=['POST'])
def close_dispute(request):
    try:
        payload = json.loads(request.body)
        is_approved = payload['approved']
        dispute = Dispute.objects.get(pk=payload['dispute_id'])

        if is_approved:
            dispute.approve(payload['final_absence_number'])
        else:
            dispute.refuse()

        return JsonResponse({'status': "success"})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=400)


@api_view(http_method_names=['GET'])
def get_open_disputes(request):
    try:
        open_disputes = Dispute.objects \
            .filter(absence__lecture__instructor=request.user.person, status=Dispute.WAITING) \
            .select_related('absence').select_related('absence__student').select_related('absence__lecture')

        dispute_list = list()

        for dispute in open_disputes:
            dispute_list.append({
                'student_name': dispute.absence.student.get_full_name(),
                'subject_name': dispute.absence.lecture.group.subject.name,
                'date': dispute.absence.lecture.date,
                'absence_number': dispute.absence.absence_number,
                'message': dispute.message,
                'status': dispute.status,
                'dispute_id': dispute.pk
            })

        return JsonResponse({'status': "success", 'disputes': dispute_list})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
