import json
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import authentication, permissions

from inclass_server.models import Course, Subject


class SubjectAPI(APIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAdminUser,)

    def get(self, request):
        try:
            external_code_list = None
            if request.GET.get('external_code'):
                external_code_list = request.GET.get('external_code')

            if not external_code_list:
                subject_queryset = Subject.objects.all()
            else:
                subject_queryset = Subject.objects.filter(external_code__in=external_code_list)

            subject_list = list()
            for subject in subject_queryset:
                subject_list.append(subject.to_dict())

            return JsonResponse({'status': 'success', 'subjects': subject_list})  # , safe = False
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

    def post(self, request):
        try:
            payload = json.loads(request.body)
            subject_list = payload.get('subjects')
            if subject_list:
                for subject_dict in subject_list:
                    Subject.save_from_dict(subject_dict)
            return JsonResponse({'status': 'success'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

    def delete(self, request):
        try:
            payload = json.loads(request.body)
            external_code_list = payload.get('external_code')
            if external_code_list:
                Subject.objects.filter(external_code__in=external_code_list).delete()
            return JsonResponse({'status': 'success'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
