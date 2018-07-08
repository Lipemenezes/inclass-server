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
def joguinhos(request):
    return JsonResponse(
        {
            'jogos': [
                {
                    'id': 1,
                    'nome': 'The Elder Scroll V: Skyrim',
                    'desenvolvedora': 'Bethesda',
                    'ano': 2010
                },
                {
                    'id': 2,
                    'nome': 'Grand Theft Auto V',
                    'desenvolvedora': 'Rockstar Games',
                    'ano': 2013
                },
                {
                    'id': 3,
                    'nome': 'The Last of Us',
                    'desenvolvedora': 'Sony Computer Entertainment',
                    'ano': 2013
                },
                {
                    'id': 4,
                    'nome': 'Red  Dead Redemption',
                    'desenvolvedora': 'Rockstar San Diego',
                    'ano': 2010
                },
                {
                    'id': 5,
                    'nome': 'Resident Evil 8',
                    'desenvolvedora': 'No idea',
                    'ano': 2021
                },
                {
                    'id': 6,
                    'nome': 'Red  Dead Redemption 2',
                    'desenvolvedora': 'Rockstar Games',
                    'ano': 2018
                },
                {
                    'id': 7,
                    'nome': 'GTA VI',
                    'desenvolvedora': 'Rockstar Games',
                    'ano': 2023
                },
            ]
        }
    )
