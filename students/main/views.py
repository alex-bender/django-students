from django.shortcuts import render_to_response
from models import Group, Student

def show_groups(request):
    groups = Group.objects.all()

    what = 'Group' 
    groups = Group.objects.all()
    return render_to_response('view_groups_and_students.html',
                              {'item': groups, 'what': what})
    
def show_students(request):
    students = Student.objects.all()

    what = 'Student' 
    students = Student.objects.all()
    return render_to_response('view_groups_and_students.html',
                              {'item': students, 'what': what})