from rest_framework import serializers

from people.models import Student
from groups.models import Group


class GroupSerializer(serializers.HyperlinkedModelSerializer):

    id = serializers.Field()

    class Meta:
        model = Group
        fields = ('id', 'url', 'name', 'senior')


class StudentSerializer(serializers.HyperlinkedModelSerializer):

    id = serializers.Field()

    class Meta:
        model = Student
        fields = ('id', 'url', 'name', 'last_name', 'birthday_date',
                  'student_id_card', 'group')

