from django.core.urlresolvers import reverse

from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, redirect, get_object_or_404, render
from django.template import RequestContext

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm

from forms import StudentForm, GroupForm
from models import Student, Group

from django.contrib.auth.decorators import login_required

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------

def index(request):
    return render(request, 'base.html')
#------------------------------------------------------------------------------
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
@login_required(redirect_field_name='/students_add/')
def students_add(request):
    form = StudentForm(request.POST or None)
    if form.is_valid():
        form.save()
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
        form.save()
        return redirect(students)
    return render_to_response('students_edit.html',
                              {'student_form': form,
                               'student_id': student_id},
                              context_instance=RequestContext(request))
#------------------------------------------------------------------------------
@login_required
def students_delete(request, student_id):
    Student.objects.get(pk=student_id).delete()

    return redirect(students)
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
@login_required
def groups(request):
    groups = Group.objects.all().order_by('pk')
    counter = []
    for group in groups:
        counter.append(Student.objects.filter(group__name=group.name).count())
    counter.reverse()
    return render_to_response('groups.html',
                              {'groups': groups,
                               'counter': counter})
#------------------------------------------------------------------------------
@login_required
def groups_add(request):
    form = GroupForm(request.POST or None)
    if form.is_valid():
        form.save()
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
        form.save()
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
    Group.objects.get(pk=group_id).delete()
    
    return redirect(groups)
#------------------------------------------------------------------------------
def edit_object(request, obj):
    url = reverse('admin:%s_%s_change' % (object._meta.app_label, object._meta.module_name), args=[object.id])
    return u'<a href="%s">Edit %s</a>' % (url,  self.object.__unicode__())
