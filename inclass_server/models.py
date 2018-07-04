# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import uuid
from __builtin__ import unicode
from datetime import datetime

from django.contrib.auth.models import User
from django.db import models


from django.conf import settings
from django.db.models import Sum
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import Permission

from api_mobile.utils.email_helper import send_email


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class Institution(models.Model):
    name = models.CharField(max_length=200, verbose_name='nome')
    register = models.CharField(max_length=14, verbose_name='cnpj')
    external_code = models.CharField(max_length=200, verbose_name='código externo')
    is_deleted = models.BooleanField(default=False, null=False)

    def to_dict(self):
        address = Address.objects.get(institution__id=self.pk)
        return {
            'name': self.name,
            'register': self.register,
            'street': address.street,
            'number': address.number,
            'city': address.city,
            'state': address.state,
            'postal_code': address.postal_code,
            'complement': address.complement,
        }

    @staticmethod
    def save_from_dict(institution_dict):
        institution = Institution.objects.all().first()

        if not institution:
            institution = Institution()
            address = Address()
        else:
            address = Address.objects.filter(institution__id=institution.pk).first()

        if institution_dict.get('name'):
            institution.name = institution_dict['name']
        if institution_dict.get('register'):
            institution.register = institution_dict['register']
        if institution_dict.get('external_code'):
            institution.external_code = institution_dict['external_code']
        if institution_dict.get('street'):
            address.street = institution_dict['street']
        if institution_dict.get('number'):
            address.number = institution_dict['number']
        if institution_dict.get('city'):
            address.city = institution_dict['city']
        if institution_dict.get('state'):
            address.state = institution_dict['state']
        if institution_dict.get('postal_code'):
            address.postal_code = institution_dict['postal_code']
        if institution_dict.get('complement'):
            address.complement = institution_dict['complement']

        institution.save()
        address.institution = institution
        address.save()
        institution.address = address
        institution.save()

        return institution

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

    def to_dict(self):
        return {
            'course_id': self.pk,
            'name': self.name,
            'initials': self.initials,
            'external_code': self.external_code
        }

    @staticmethod
    def save_from_dict(course_dict):
        course = Course.objects.filter(external_code=course_dict.get('external_code')).first()

        if not course:
            course = Course()

        if course_dict.get('name'):
            course.name = course_dict['name']
        if course_dict.get('initials'):
            course.initials = course_dict['initials']
        if course_dict.get('external_code'):
            course.external_code = course_dict['external_code']

        course.institution = Institution.objects.filter(external_code=course_dict['institution_code']).first()

        course.save()

        return course

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

    def to_dict(self):
        courses_list = list()
        for course in self.courses.all():
            courses_list.append(course.to_dict())

        return {
            'name': self.name,
            'initials': self.initials,
            'workload': self.workload,
            'external_code': self.external_code,
            'courses': courses_list
        }

    @staticmethod
    def save_from_dict(subject_dict):
        subject = Subject.objects.filter(external_code=subject_dict.get('external_code')).first()

        if not subject:
            subject = Subject()

        if subject_dict.get('name'):
            subject.name = subject_dict['name']
        if subject_dict.get('initials'):
            subject.initials = subject_dict['initials']
        if subject_dict.get('workload'):
            subject.workload = subject_dict['workload']
        if subject_dict.get('external_code'):
            subject.external_code = subject_dict['external_code']

        if not subject.pk:
            subject.save()

        if subject_dict.get('courses'):
            courses = Course.objects.filter(external_code__in=subject_dict.get('courses'))
            subject.courses.add(*list(courses))

        return subject

    class Meta:
        db_table = 'subject'
        verbose_name = 'disciplina'
        verbose_name_plural = 'disciplinas'


class Person(models.Model):
    social_security_number = models.CharField(max_length=200, verbose_name='cpf')
    register = models.CharField(max_length=200, verbose_name='matrícula')
    external_code = models.CharField(max_length=200, verbose_name='código externo')
    is_deleted = models.BooleanField(default=False, null=False)
    is_new_password = models.BooleanField(default=False, null=False)
    user = models.OneToOneField(User, null=False)

    def delete(self, *args, **kwargs):
        self.user.delete()
        super(Person, self).delete()

    def get_full_name(self):
        return '{} {}'.format(self.user.first_name, self.user.last_name)

    def to_dict(self):
        return {
            'external_code': self.external_code,
            'social_security_number': self.social_security_number,
            'register': self.register,
            'username': self.user.username,
            'is_student': self.user.has_perm('inclass_server.is_student'),
            'is_professor': self.user.has_perm('inclass_server.is_professor'),
            'is_admin': self.user.has_perm('inclass_server.is_admin'),
            'email': self.user.email,
            'first_name': self.user.first_name,
            'last_name': self.user.last_name
        }

    @staticmethod
    def reset_password_email(social_security_number):
        try:
            person = Person.objects.get(social_security_number=social_security_number)
            new_password = str(uuid.uuid4().int)[:8]
            person.user.set_password(new_password)
            person.user.save()
            person.is_new_password = True
            person.save()

            email_subject = 'Sua nova senha do InClass'
            email_body = unicode("Sua nova senha: {}").format(new_password)

            email_login = SystemConfig.objects.get(config='email').value
            email_password = SystemConfig.objects.get(config='email_pass').value

            is_sent, error = send_email(
                body=email_body,
                subject=email_subject,
                to=person.user.email,
                email_login=email_login,
                email_password=email_password
            )
            return is_sent
        except:
            return None

    @staticmethod
    def save_from_dict(person_dict):
        person = Person.objects.filter(external_code=person_dict.get('external_code')) \
            .select_related('user').first()

        if not person:
            person = Person()
            user = User.objects.create_user(
                username=person_dict['social_security_number'],
                password=person_dict['password'],
                first_name=person_dict['first_name'],
                last_name=person_dict['last_name'],
                email=person_dict['email']
            )
            person.is_new_password = True
        else:
            user = person.user

        if person_dict.get('external_code'):
            person.external_code = person_dict['external_code']
        if person_dict.get('social_security_number'):
            person.social_security_number = person_dict['social_security_number']
        if person_dict.get('register'):
            person.register = person_dict['register']
        if person_dict.get('is_student'):
            permission = Permission.objects.get(codename='is_student')
            user.user_permissions.add(permission)
        if person_dict.get('is_professor'):
            permission = Permission.objects.get(codename='is_professor')
            user.user_permissions.add(permission)
        if person_dict.get('is_admin'):
            permission = Permission.objects.get(codename='is_admin')
            user.user_permissions.add(permission)
        if person_dict.get('email'):
            user.email = person_dict['email']
        if person_dict.get('first_name'):
            user.first_name = person_dict['first_name']
        if person_dict.get('last_name'):
            user.last_name = person_dict['last_name']

        user.save()
        person.user = user
        person.save()

        return person

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
    course = models.ForeignKey(Course, null=False)
    instructors = models.ManyToManyField(Person, db_column='instructors', related_name='instructor_in_groups')
    students = models.ManyToManyField(Person, db_column='students', related_name='member_in_groups')
    monday = models.BooleanField(default=False, null=False)
    tuesday = models.BooleanField(default=False, null=False)
    wednesday = models.BooleanField(default=False, null=False)
    thursday = models.BooleanField(default=False, null=False)
    friday = models.BooleanField(default=False, null=False)
    saturday = models.BooleanField(default=False, null=False)
    sunday = models.BooleanField(default=False, null=False)

    def get_days_of_the_week_string(self):
        days_of_the_week_list = []

        if self.monday:
            days_of_the_week_list.append('Seg')
        if self.tuesday:
            days_of_the_week_list.append('Ter')
        if self.wednesday:
            days_of_the_week_list.append('Qua')
        if self.thursday:
            days_of_the_week_list.append('Qui')
        if self.friday:
            days_of_the_week_list.append('Sex')
        if self.saturday:
            days_of_the_week_list.append('Sab')
        if self.sunday:
            days_of_the_week_list.append('Dom')

        return ', '.join(days_of_the_week_list)

    def to_dict(self):
        instructors = list()
        for instructor in self.instructors.all().select_related('user'):
            instructors.append({
                'full_name': instructor.get_full_name(),
                'external_code': instructor.external_code
            })

        students = list()
        for student in self.students.all().select_related('user'):
            students.append({
                'full_name': student.get_full_name(),
                'external_code': student.external_code
            })

        return {
            'year': self.year,
            'day_period': self.day_period,
            'semester': self.semester,
            'start_at': self.start_at.strftime('%d/%m/%Y'),
            'end_at': self.end_at.strftime('%d/%m/%Y'),
            'external_code': self.external_code,
            'subject': self.subject.to_dict(),
            'monday': self.monday,
            'tuesday': self.tuesday,
            'wednesday': self.wednesday,
            'thursday': self.thursday,
            'friday': self.friday,
            'saturday': self.saturday,
            'sunday': self.sunday,
            'students': students,
            'instructors': instructors,
            'course': self.course.to_dict()
        }

    @staticmethod
    def save_from_dict(group_dict):
        group = Group.objects.filter(external_code=group_dict.get('external_code')).first()

        if not group:
            group = Group()
            group.subject = Subject.objects.get(external_code=group_dict.get('subject_code'))
            group.course = Course.objects.get(external_code=group_dict.get('course_code'))

        if group_dict.get('year'):
            group.year = group_dict['year']
        if group_dict.get('day_period') is not None:
            group.day_period = group_dict['day_period']
        if group_dict.get('semester'):
            group.semester = group_dict['semester']
        if group_dict.get('start_at'):
            group.start_at = datetime.strptime(group_dict['start_at'], '%Y-%m-%d')
        if group_dict.get('end_at'):
            group.end_at = datetime.strptime(group_dict['end_at'], '%Y-%m-%d')
        if group_dict.get('external_code'):
            group.external_code = group_dict['external_code']

        if group_dict.get('monday'):
            group.monday = group_dict['monday']
        if group_dict.get('tuesday'):
            group.tuesday = group_dict['tuesday']
        if group_dict.get('wednesday'):
            group.wednesday = group_dict['wednesday']
        if group_dict.get('thursday'):
            group.thursday = group_dict['thursday']
        if group_dict.get('friday'):
            group.friday = group_dict['friday']
        if group_dict.get('saturday'):
            group.saturday = group_dict['saturday']
        if group_dict.get('sunday'):
            group.sunday = group_dict['sunday']

        if group_dict.get('subject_code'):
            group.subject = Subject.objects.filter(external_code=group_dict['subject_code']).first()

        if group_dict.get('course_code'):
            group.course = Course.objects.filter(external_code=group_dict['course_code']).first()

        group.save()

        if group_dict.get('instructor_code_add'):
            instructors = Person.objects.filter(external_code__in=group_dict['instructor_code_add'])
            instructors_to_add = Group.get_person_not_in_many_to_many(
                person_queryset=instructors,
                current_persons=group.instructors.all()
            )
            group.instructors.add(*instructors_to_add)

        if group_dict.get('student_code_add'):
            students = Person.objects.filter(external_code__in=group_dict['student_code_add'])
            students_to_add = Group.get_person_not_in_many_to_many(
                person_queryset=students,
                current_persons=group.students.all()
            )
            group.students.add(*students_to_add)

        if group_dict.get('instructor_code_remove'):
            instructors = Person.objects.filter(external_code__in=group_dict['instructor_code_remove'])
            group.instructors.remove(*instructors)

        if group_dict.get('student_code_remove'):
            students = Person.objects.filter(external_code__in=group_dict['student_code_remove'])
            group.students.remove(*students)

        return group

    @staticmethod
    def get_person_not_in_many_to_many(person_queryset, current_persons):
        person_list_to_add = list()
        for person in person_queryset:
            if person not in current_persons:
                person_list_to_add.append(person)
        return person_list_to_add

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

    def get_absences(self):
        absences = Absence.objects.filter(lecture_id=self.pk).values('absence_number', 'student__external_code')
        return list(absences)

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
            )
            lecture.save()

        return lecture

    def to_dict(self):
        return {
            'date': self.date.strftime('%d/%m/%Y'),
            'workload': self.workload,
            'instructor_code': self.instructor.external_code,
            'group_code': self.group.external_code,
            'absences': self.get_absences()
        }

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
        return Absence.objects.filter(student=person, lecture__group=group) \
            .aggregate(Sum('absence_number'))['absence_number__sum']

    def to_dict(self):
        return {
            'absence_id': self.pk,
            'subject': self.lecture.group.subject.name,
            'instructor': self.lecture.instructor.get_full_name(),
            'absence_number': self.absence_number,
            'date': self.lecture.date,
            'has_dispute': self.has_dispute()
        }

    def has_dispute(self):
        return Dispute.objects.filter(absence=self).exists()

    @staticmethod
    def update_or_create(lecture, student_id, absence_number):
        absence = Absence.objects.filter(
            lecture_id=lecture.pk,
            student_id=student_id,
        ).first()

        if absence:
            absence.absence_number = absence_number or 0
            absence.save()
        elif absence_number and absence_number > 0:
            absence = Absence(
                lecture_id=lecture.pk,
                student_id=student_id,
                absence_number=absence_number
            ).save()
        else:
            absence = None

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
        self.absence.absence_number = final_absence_number
        self.absence.save()

    def refuse(self):
        self.status = Dispute.REFUSED
        self.final_absence_number = self.initial_absence_number
        self.save()

    class Meta:
        db_table = 'dispute'
        verbose_name = 'contestação'
        verbose_name_plural = 'contestações'


class SystemConfig(models.Model):
    config = models.CharField(max_length=200, verbose_name='chave')
    value = models.CharField(max_length=200, verbose_name='valor')

    def to_dict(self):
        return {
            'config': self.config,
            'value': self.value
        }

    class Meta:
        db_table = 'system_config'
        verbose_name = 'configuração do sistemas'
        verbose_name_plural = 'configurações do sistema'
