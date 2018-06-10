from django.http import JsonResponse
from rest_framework.decorators import api_view


@api_view(http_method_names=['GET'])
def get_professor_data(request):
    a = 'teste'
    return JsonResponse({'id': request.GET.get('professor_id')})