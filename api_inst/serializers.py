from django.contrib.auth.models import User
from rest_framework import serializers

from inclass_server.models import Institution, Dispute, Absence, Lecture, Group, Person, Subject, Course, Address


class UserSerializer(serializers.HyperlinkedModelSerializer):
    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()

        return user

    class Meta:
        model = User
        fields = '__all__'
        read_only_fields = ('id', )
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }


class InstitutionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Institution
        fields = '__all__'
        read_only_fields = ('id', )


class AddressSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'
        read_only_fields = ('id', )


class CourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'
        read_only_fields = ('id', )


class SubjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'
        read_only_fields = ('id', )


class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'
        read_only_fields = ('id', )


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'
        read_only_fields = ('id', )


class LectureSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Lecture
        fields = '__all__'
        read_only_fields = ('id', )


class AbsenceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Absence
        fields = '__all__'
        read_only_fields = ('id', )


class DisputeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dispute
        fields = '__all__'
        read_only_fields = ('id', )

