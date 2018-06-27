# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import JsonResponse

# Create your views here.
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response

from inclass_server.models import Person, Institution, Group, Absence, Dispute


@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def obtain_auth_token(request, *args, **kwargs):
    user = authenticate(username=request.POST['username'], password=request.POST['password'])
    if user:
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'is_student': user.has_perm('inclass_server.is_student'),
            'is_professor': user.has_perm('inclass_server.is_professor'),
            'is_admin': user.has_perm('inclass_server.is_admin'),
            'name': user.person.get_full_name(),
            'email': user.email,
            'register': user.person.register,
            'institution': Institution.objects.first().name,
            'is_new_password': user.person.is_new_password,
            'social_security_number': user.person.social_security_number
        })
    else:
        return Response({
            'error': 'invalid credentials'
        })


@api_view(http_method_names=['GET'])
def get_admin_data(request):
    a = 'teste'
    return JsonResponse({'id': request.GET.get('professor_id')})