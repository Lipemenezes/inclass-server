# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models


from django.conf import settings
from django.db.models import Sum
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class Institution(models.Model):
    name = models.CharField(max_length=200, verbose_name='nome')
    register = models.CharField(max_length=14, verbose_name='cnpj')
    api_token = models.CharField(max_length=50, verbose_name='TOKEN')
    external_code = models.CharField(max_length=200, verbose_name='código externo')
    is_deleted = models.BooleanField(default=False, null=False)

    class Meta:
        db_table = 'institution'
        verbose_name = "instituição"
        verbose_name_plural = "instituições"


class Address(models.Model):
    street = models.CharField(max_length=200, verbose_name='rua')
    number = models.IntegerField(verbose_name='número')
    district = models.CharField(max_length=200, verbose_name='bairro')
    city = models.CharField(max_length=200, verbose_name='cidade')
    state = models.CharField(max_length=200, verbose_name='estado')
    postal_code = models.CharField(max_length=200, verbose_name='cep')
    complement = models.CharField(max_length=200, verbose_name='complemento')
    external_code = models.CharField(max_length=200, verbose_name='código externo')
    is_deleted = models.BooleanField(default=False, null=False)
    institution = models.ForeignKey(Institution, null=False)

    class Meta:
        db_table = 'address'
        verbose_name = "endereço"
        verbose_name_plural = "endereços"


class Course(models.Model):
    name = models.CharField(max_length=200, verbose_name='nome')
    initials = models.CharField(max_length=14, verbose_name='sigla')
    external_code = models.CharField(max_length=200, verbose_name='código externo')
    is_deleted = models.BooleanField(default=False, null=False)
    institution = models.ForeignKey(Institution, null=False)

    class Meta:
        db_table = 'course'
        verbose_name = "curso"
        verbose_name_plural = "cursos"


class Subject(models.Model):
    name = models.CharField(max_length=200, verbose_name='nome')
    initials = models.CharField(max_length=14, verbose_name='sigla')
    workload = models.IntegerField(verbose_name='carga horária')
    external_code = models.CharField(max_length=200, verbose_name='código externo')
    is_deleted = models.BooleanField(default=False, null=False)
    courses = models.ManyToManyField(Course, related_name='contained_subjects')

    class Meta:
        db_table = 'subject'
        verbose_name = 'disciplina'
        verbose_name_plural = 'disciplinas'


class Person(models.Model):
    social_security_number = models.CharField(max_length=200, verbose_name='cpf')
    register = models.CharField(max_length=200, verbose_name='matrícula')
    external_code = models.CharField(max_length=200, verbose_name='código externo')
    is_deleted = models.BooleanField(default=False, null=False)
    user = models.OneToOneField(User, null=False)

    class Meta:
        db_table = 'person'
        verbose_name = 'pessoa'
        verbose_name_plural = 'pessoas'
        permissions = (
            ("is_professor", "Has professor permissions"),
            ("is_student", "Has student permissions"),
            ("is_admin", "Has administrator permissions"),
        )


class Group(models.Model):
    MORNING = 0
    EVENING = 1
    NIGHT = 2

    year = models.IntegerField(verbose_name='ano')
    day_period = models.IntegerField(verbose_name='período')
    semester = models.IntegerField(verbose_name='semestre')
    start_at = models.DateField(verbose_name='data de início')
    end_at = models.DateField(verbose_name='data de fim')
    external_code = models.CharField(max_length=200, verbose_name='código externo')
    is_deleted = models.BooleanField(default=False, null=False)
    subject = models.ForeignKey(Subject, null=False)
    instructors = models.ManyToManyField(Person, db_column='instructors', related_name='instructor_in_groups')
    students = models.ManyToManyField(Person, db_column='students', related_name='member_in_groups')
    # days of the week

    class Meta:
        db_table = 'group'
        verbose_name = 'turma'
        verbose_name_plural = 'turmas'


class Lecture(models.Model):
    date = models.DateField(verbose_name='data')
    workload = models.IntegerField(verbose_name='aula')
    is_deleted = models.BooleanField(default=False, null=False)
    group = models.ForeignKey(Group)
    instructor = models.ForeignKey(Person)

    @staticmethod
    def update_or_create(instructor_id, group_id, date, workload):
        lecture = Lecture.objects.filter(
            instructor_id=instructor_id,
            group_id=group_id,
            date=date
        ).first()

        if lecture:
            lecture.workload = workload
            lecture.save()
        else:
            lecture = Lecture(
                instructor_id=instructor_id,
                group_id=group_id,
                date=date,
                workload=workload
            ).save()

        return lecture

    class Meta:
        db_table = 'lecture'
        verbose_name = 'aula'
        verbose_name_plural = 'aulas'


class Absence(models.Model):
    absence_number = models.IntegerField(verbose_name='falta')
    is_deleted = models.BooleanField(default=False, null=False)
    lecture = models.ForeignKey(Lecture)
    student = models.ForeignKey(Person)

    @staticmethod
    def get_total(person, group):
        return Absence.objects.filter(student=person, lecture__group=group).aggregate(Sum('absence_number'))

    def has_dispute(self):
        return Dispute.objects.filter(absence=self).exists()

    @staticmethod
    def update_or_create(lecture_id, student_id, absence_number):
        absence = Absence.objects.filter(
            lecture_id=lecture_id,
            student_id=student_id,
        ).first()

        if absence:
            absence.absence_number = absence_number
            absence.save()
        else:
            absence = Absence(
                lecture_id=lecture_id,
                student_id=student_id,
                absence_number=absence_number
            ).save()

        return absence

    class Meta:
        db_table = 'absence'
        verbose_name = 'falta'
        verbose_name_plural = 'faltas'
        unique_together = (("lecture", "student"),)


class Dispute(models.Model):
    WAITING = 0
    APPROVED = 1
    REFUSED = 2

    message = models.CharField(max_length=200, verbose_name='mensagem')
    status = models.IntegerField()
    initial_absence_number = models.IntegerField()
    final_absence_number = models.IntegerField()
    is_deleted = models.BooleanField(default=False, null=False)
    absence = models.ForeignKey(Absence)

    def approve(self, final_absence_number):
        self.status = Dispute.APPROVED
        self.final_absence_number = final_absence_number
        self.save()

    def refuse(self):
        self.status = Dispute.REFUSED
        self.save()

    class Meta:
        db_table = 'dispute'
        verbose_name = 'contestação'
        verbose_name_plural = 'contestações'
