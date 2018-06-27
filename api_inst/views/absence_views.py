import json

from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from datetime import datetime

from inclass_server.models import Absence, Lecture


@api_view(http_method_names=['GET'])
@permission_classes((IsAuthenticated, IsAdminUser))
def get_absences(request):
    try:
        if not request.GET.get('lecture_date'):
            return JsonResponse({'status': 'error', 'message': 'lecture_date is required'}, status=400)
        if not request.GET.get('group_external_code'):
            return JsonResponse({'status': 'error', 'message': 'group_external_code is required'}, status=400)

        try:
            lecture_date = datetime.strptime(request.GET['lecture_date'], '%Y-%m-%d')
        except:
            return JsonResponse({'status': 'error', 'message': 'lecture_date format must be yyyy-mm-dd'}, status=400)

        lecture = Lecture.objects.filter(
            date=lecture_date,
            group__external_code=request.GET['group_external_code']
        ).first()

        absences = lecture.to_dict() if lecture else []

        return JsonResponse({'status': 'success', 'absences': absences})

    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
