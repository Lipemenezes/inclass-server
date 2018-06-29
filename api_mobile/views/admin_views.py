# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from django.http import JsonResponse
from rest_framework.decorators import api_view
from inclass_server.models import SystemConfig


@api_view(http_method_names=['GET'])
def get_configs(request):
    try:
        config = SystemConfig.objects.get(config='min_allowed_attendance')
        config_dict = config.to_dict()
        response_dict = {'status': 'success'}
        response_dict[config_dict['config']] = config_dict['value']
        return JsonResponse(response_dict)
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=400)


@api_view(http_method_names=['POST'])
def set_configs(request):
    try:
        payload = json.loads(request.body)
        config = SystemConfig.objects.filter(config=payload['config']).first()

        if not config:
            config = SystemConfig(config=payload['config'])

        config.value = payload['value']
        config.save()
        return JsonResponse({'status': 'success'})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
