# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from api_inst.serializers import UserSerializer, InstitutionSerializer, AddressSerializer, CourseSerializer, \
    SubjectSerializer, PersonSerializer, GroupSerializer, LectureSerializer, AbsenceSerializer, DisputeSerializer
from inclass_server.models import Address, Institution, Course, Subject, Person, Group, Lecture, Absence, Dispute


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, IsAdminUser, )
    serializer_class = UserSerializer
    queryset = User.objects.all()
    filter_backends = (DjangoFilterBackend, )
    filter_fields = '__all__'


class InstitutionViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, IsAdminUser, )
    serializer_class = InstitutionSerializer
    queryset = Institution.objects.all()
    filter_backends = (DjangoFilterBackend, )
    filter_fields = '__all__'


class AddressViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, IsAdminUser, )
    serializer_class = AddressSerializer
    queryset = Address.objects.all()
    filter_backends = (DjangoFilterBackend, )
    filter_fields = '__all__'


class CourseViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, IsAdminUser, )
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    filter_backends = (DjangoFilterBackend, )
    filter_fields = '__all__'


class SubjectViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, IsAdminUser, )
    serializer_class = SubjectSerializer
    queryset = Subject.objects.all()
    filter_backends = (DjangoFilterBackend, )
    filter_fields = '__all__'


class PersonViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, IsAdminUser, )
    serializer_class = PersonSerializer
    queryset = Person.objects.all()
    filter_backends = (DjangoFilterBackend, )
    filter_fields = '__all__'


class GroupViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, IsAdminUser, )
    serializer_class = GroupSerializer
    queryset = Group.objects.all()
    filter_backends = (DjangoFilterBackend, )
    filter_fields = '__all__'


class LectureViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, IsAdminUser, )
    serializer_class = LectureSerializer
    queryset = Lecture.objects.all()
    filter_backends = (DjangoFilterBackend, )
    filter_fields = '__all__'


class AbsenceViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, IsAdminUser, )
    serializer_class = AbsenceSerializer
    queryset = Absence.objects.all()
    filter_backends = (DjangoFilterBackend, )
    filter_fields = '__all__'


class DisputeViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, IsAdminUser, )
    serializer_class = DisputeSerializer
    queryset = Dispute.objects.all()
    filter_backends = (DjangoFilterBackend, )
    filter_fields = '__all__'
