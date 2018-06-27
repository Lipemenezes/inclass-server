import json
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import authentication, permissions

from inclass_server.models import Group


class GroupAPI(APIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAdminUser,)

    def get(self, request):
        try:
            external_code_list = request.GET.get('external_code').split(',')

            if not external_code_list:
                group_queryset = Group.objects.all()
            else:
                group_queryset = Group.objects.filter(external_code__in=external_code_list)

            group_list = list()
            for group in group_queryset:
                group_list.append(group.to_dict())

            return JsonResponse({'status': 'success', 'groups': group_list})  # , safe = False
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

    def post(self, request):
        try:
            payload = json.loads(request.body)
            groups_list = payload.get('groups')
            if groups_list:
                for group_dict in groups_list:
                    Group.save_from_dict(group_dict)
            return JsonResponse({'status': 'success'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

    def delete(self, request):
        try:
            external_code_list = request.DELETE.get('external_code').split(',')
            if external_code_list:
                Group.objects.filter(external_code__in=external_code_list).delete()
            return JsonResponse({'status': 'success'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
