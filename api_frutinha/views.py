# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from django.contrib.auth import authenticate
from django.http import JsonResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from inclass_server.models import Person


@api_view(http_method_names=['POST'])
@authentication_classes([])
@permission_classes([])
def register(request):
    try:
        payload = json.loads(request.body)
        Person.save_from_dict(payload)
        return JsonResponse({'status': 'success'})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=400)


@api_view(http_method_names=['POST'])
@authentication_classes([])
@permission_classes([])
def authenticate_user(request):
    payload = json.loads(request.body)
    user = authenticate(username=payload['username'], password=payload['password'])
    if user:
        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error'}, status=400)


@api_view(http_method_names=['GET'])
@authentication_classes([])
@permission_classes([])
def fruits(request):
    return JsonResponse({
        'fruits': [
            {'name': 'maçã'}, {'name': 'banana'}, {'name': 'pera'}, {'name': 'uva'}, {'name': 'renato'}
        ]
    })
