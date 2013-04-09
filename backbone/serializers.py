from rest_framework import serializers

from people.models import Student
from groups.models import Group


class GroupSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Group
        fields = ('url', 'name', 'senior')


class StudentSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Student
        fields = ('url', 'name', 'last_name', 'birthday_date',
                  'student_id_card', 'group')
