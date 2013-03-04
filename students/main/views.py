from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect, get_object_or_404, render
from django.views.generic.simple import direct_to_template
from django.template import RequestContext

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from forms import Student, Group, StudentForm, GroupForm, UserCreateForm, LoginForm#, AddUserForm

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------

def index(request):
    return render(request, 'base.html')
#------------------------------------------------------------------------------
#            logout, login, and add to ech other function (if user.auth) ....
#------------------------------------------------------------------------------
def auth_user(request, username, password):

    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return HttpResponse('user is logined')
        else:
            return HttpResponse('disabled acc')
    else:
        return HttpResponse('bad login')

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
def UserLogin(request, *args, **kwargs):
    user_form = LoginForm(request.POST)

    if user_form.is_valid():
        
        username = user_form.user#clean_username()
        password = user_form.password#clean_password2()
        
        user = authenticate(username=username,
                            password=password)
#        redirect to lodin function
        login(request, user)
        return redirect(students)
    return render(request,
                  'login.html',
                  { 'user_form' : user_form })
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------

def CreateUserAndLogin(request, *args, **kwargs):
    user_form = UserCreateForm(request.POST)
    if user_form.is_valid():
        username = user_form.clean_username()
        password = user_form.clean_password2()
        #user_form.save()
        user = authenticate(username=username,
                            password=password)
#        redirect to lodin function
        login(request, user)
        return redirect(index)
    return render(request,
                  'atemlete.html',
                  { 'user_form' : user_form })

def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        # good pass & user "active"
        auth.login(request, user)
        # redirect to the  "right" page
        return HttpResponseRedirect("/account/loggedin/")
    else:
        # responce page with error
        return HttpResponseRedirect("/account/invalid/")

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
def students(request):
    students_list = Student.objects.all().order_by('name')
    return render_to_response('students.html',
                              {'students_list': students_list,})
#------------------------------------------------------------------------------
def students_add(request):
    form = StudentForm(request.POST or None)
    if form.is_valid():
        cmodel = form.save()
        cmodel.save()
        return redirect(students)

    return render_to_response('students_add.html',
                              {'student_form': form},
                              context_instance=RequestContext(request))    
#------------------------------------------------------------------------------
def students_edit(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    form = StudentForm(request.POST or None, instance=student)
    if form.is_valid():
        concat = form.save()
        concat.save()
        return redirect(students)
    return render_to_response('students_edit.html',
                              {'student_form': form,
                               'student_id': student_id},
                              context_instance=RequestContext(request))
#------------------------------------------------------------------------------
def students_delete(request, student_id):
    stud = Student.objects.get(pk=student_id).delete()

    return redirect(students)
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
def groups(request):
    groups_list = Group.objects.all().order_by('name')
    return render_to_response('groups.html',
                              {'groups_list': groups_list,})
#------------------------------------------------------------------------------
def groups_add(request):
    form = GroupForm(request.POST or None)
    if form.is_valid():
        cmodel = form.save()
        cmodel.save()
        return redirect(groups)
    
    return render_to_response('groups_add.html',
                              {'group_form': form},
                              context_instance=RequestContext(request))
#------------------------------------------------------------------------------
def groups_edit(request, group_id):
    group = get_object_or_404(Group, pk=group_id)
    form = GroupForm(request.POST or None, instance=group)
    if form.is_valid():
        concat = form.save()
        concat.save()
        return redirect(groups)
    return render_to_response('groups_edit.html',
                              {'group_form': form,
                               'group_id': group_id},
                              context_instance=RequestContext(request))    
#------------------------------------------------------------------------------
def groups_delete(request, group_id):
    group = Group.objects.get(pk=group_id).delete()
    
    return redirect(groups)
#------------------------------------------------------------------------------
