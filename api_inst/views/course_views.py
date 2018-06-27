import json
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import authentication, permissions

from inclass_server.models import Course


class CourseAPI(APIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAdminUser,)

    def get(self, request):
        try:
            external_code_list = None
            if request.GET.get('person_code'):
                external_code_list = request.GET.get('person_code').split(',')
                external_code_list = [str(code) for code in external_code_list]

            if not external_code_list:
                course_queryset = Course.objects.all()
            else:
                course_queryset = Course.objects.filter(external_code__in=external_code_list)

            course_list = course_queryset.values('name', 'initials', 'external_code')
            course_list = list(course_list)

            return JsonResponse({'status': 'success', 'courses': course_list})  # , safe = False
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

    def post(self, request):
        try:
            payload = json.loads(request.body)
            course_list = payload.get('courses')
            for course_dict in course_list:
                Course.save_from_dict(course_dict)
            return JsonResponse({'status': 'success'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

    def delete(self, request):
        try:
            payload = json.loads(request.body)
            external_code_list = payload.get('external_code')
            if external_code_list:
                Course.objects.filter(external_code__in=external_code_list).delete()
            return JsonResponse({'status': 'success'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
