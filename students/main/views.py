from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, redirect, get_object_or_404, render
from django.views.generic.simple import direct_to_template
from django.template import RequestContext

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from forms import StudentForm, GroupForm#, AddUserForm, UserCreateForm, LoginForm
from models import Student, Group

from django.contrib.auth.decorators import login_required

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------

def index(request):
    return render(request, 'base.html')

def olologin(request):
    login_form = AuthenticationForm(data=request.POST)
    if (login_form.is_valid()):
        user = authenticate(
                username=login_form.cleaned_data['username'], 
                password=login_form.cleaned_data['password'])
        login(request, user)
        HttpResponse('login success')
    return render(request,
                  'login.html',
                  { 'user_form' : login_form })

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/index/')
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
def CreateUserAndLogin(request, *args, **kwargs):
    user_form = UserCreationForm(request.POST)
    if user_form.is_valid():
        username = user_form.clean_username()
        password = user_form.clean_password2()
        user_form.save()
        user = authenticate(username=username,
                            password=password)
        login(request, user)
        return redirect(index)
    return render(request,
                  'atemlete.html',
                  { 'user_form' : user_form })
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
@login_required
def students(request):
    students_list = Student.objects.all().order_by('name')
    return render_to_response('students.html',
                              {'students_list': students_list,})
#------------------------------------------------------------------------------
@login_required
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
@login_required
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
@login_required
def students_delete(request, student_id):
    student = Student.objects.get(pk=student_id).delete()

    return redirect(students)
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
@login_required
def groups(request):
    groups = Group.objects.all().order_by('name')
    return render_to_response('groups.html',
                              {'groups': groups,})
#------------------------------------------------------------------------------
@login_required
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
@login_required
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
@login_required
def group_list(request, group_name):
    students_list = Student.objects.filter(group__name=group_name)
    
    return render_to_response('students_in_group.html',
                              {'students_list': students_list,
                              'group_name': group_name},)
#------------------------------------------------------------------------------
@login_required
def groups_delete(request, group_id):
    group = Group.objects.get(pk=group_id).delete()
    
    return redirect(groups)
#------------------------------------------------------------------------------