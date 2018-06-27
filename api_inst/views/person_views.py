import json
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import authentication, permissions
from inclass_server.models import Person


class PersonAPI(APIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAdminUser,)

    def get(self, request):
        try:
            person_code_list = None
            if request.GET.get('person_code'):
                person_code_list = request.GET.get('person_code').split(',')
                person_code_list = [str(code) for code in person_code_list]

            if person_code_list:
                persons = Person.objects.filter(external_code__in=person_code_list).select_related('user')
            else:
                persons = Person.objects.all()

            person_list = list()
            for person in persons:
                person_list.append(person.to_dict())

            return JsonResponse({'status': 'success', 'person': person_list})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

    def post(self, request):
        payload = json.loads(request.body)
        person_list = payload.get('person')
        try:
            for person_dict in person_list:
                Person.save_from_dict(person_dict)
            return JsonResponse({'status': 'success'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

    def delete(self, request):
        try:
            payload = json.loads(request.body)
            person_code_list = payload.get('person_code')
            if person_code_list:
                [person.delete() for person in Person.objects.filter(external_code__in=person_code_list)]
            return JsonResponse({'status': 'success'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})
