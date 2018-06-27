import json
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import authentication, permissions

from inclass_server.models import Institution


class InstitutionAPI(APIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAdminUser,)

    def get(self, request):
        institution = Institution.objects.all().first()
        return JsonResponse(institution.to_dict())

    def post(self, request):
        payload = json.loads(request.body)
        institution_dict = payload.get('institution')
        Institution.save_from_dict(institution_dict)
        return JsonResponse({'status': 'success'})
