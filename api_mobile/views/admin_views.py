# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from django.http import JsonResponse
from rest_framework.decorators import api_view
from inclass_server.models import Group, Absence, Dispute, SystemConfig


@api_view(http_method_names=['GET'])
def get_configs(request):
    try:
        configs = SystemConfig.objects.all().values('config', 'value')
        configs = list(configs)
        return JsonResponse({'status': 'success', 'configs': configs})
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
