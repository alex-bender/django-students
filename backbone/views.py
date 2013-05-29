from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.reverse import reverse
from rest_framework.response import Response
from backbone.serializers import GroupSerializer, StudentSerializer
from rest_framework import permissions

from backbone.permissions import IsOwnerOrReadOnly
from people.models import Student
from groups.models import Group


@api_view(['GET'])
def api_root(request, format=None):
    """
    The entry endpoint of our API.
    """
    return Response({
        'groups': reverse('group-list', request=request),
        'students': reverse('student-list', request=request),
    })


class StudentList(generics.ListCreateAPIView):
    """
    API endpoint that represents a list of students.
    """
    model = Student
    serializer_class = StudentSerializer
    permission_classes = (IsAuthenticated,)


class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that represents a single student.
    """
    model = Student
    serializer_class = StudentSerializer
    permission_classes = (IsAuthenticated,)


class GroupList(generics.ListCreateAPIView):
    """
    API endpoint that represents a list of groups.
    """
    model = Group
    serializer_class = GroupSerializer
    permission_classes = (IsAuthenticated,)


class GroupDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that represents a single group.
    """
    model = Group
    serializer_class = GroupSerializer
    permission_classes = (IsAuthenticated,)