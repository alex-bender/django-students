from django.views.generic.base import TemplateView, View

from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, redirect, get_object_or_404, render
from django.template import RequestContext

from django.contrib.auth import authenticate, login, logout

from forms import StudentForm, GroupForm
from models import Student, Group

from django.contrib.auth.decorators import login_required
from forms import UserCreateForm
from django.views.generic.edit import UpdateView

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
class HomePageView(TemplateView):

    template_name = "base.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        #context['latest_articles'] = Article.objects.all()[:5]
        return context
#==============================================================================
#------------------------------------------------------------------------------
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/index/')
#------------------------------------------------------------------------------
#==============================================================================
class CreteUserAndLogin(View):
    form_class = UserCreateForm
    initial = {
               #'username': 'YourName'
               }
    template_name = 'registration.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request,  self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            username = form.clean_username()
            password = form.clean_password2()
            form.save()
            user = authenticate(username=username,
                                password=password)
            login(request, user)
            #return redirect(index)
            return HttpResponseRedirect('/index/')

        return render(request, self.template_name, {'form': form})
#==============================================================================
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
@login_required
def students(request):
    students = Student.objects.all().order_by('name')
    return render_to_response('students.html',
                              {'students': students,},
                              context_instance=RequestContext(request))
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
    
    return render_to_response('groups.html',
                              {'groups': groups,},
                              context_instance=RequestContext(request))
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
#==============================================================================
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
#==============================================================================
class GroupsEdit(View):
    
    form_class = GroupForm
    initial = {}
    template_name = 'students_in_group.html'

    def get(self, request, *args, **kwargs):
        import ipdb;ipdb.set_trace()
        group_id = kwargs.pop('group_id')
        group = get_object_or_404(Group, pk=group_id)
        form = self.form_class(initial={'group': group})
        return render(request,  self.template_name, {'group_form': form,
                                                     'group_id': group_id},)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/groups/')

        return render(request, self.template_name, {'form': form})
#==============================================================================
#------------------------------------------------------------------------------
@login_required
def group_list(request, group_name):
    students_list = Student.objects.filter(group__name=group_name)
    
    return render_to_response('students_in_group.html',
                              {'students_list': students_list,
                              'group_name': group_name},
                              context_instance=RequestContext(request))
#------------------------------------------------------------------------------
@login_required
def bred(request, student_id):
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
def groups_delete(request, group_id):
    Group.objects.get(pk=group_id).delete()
    
    return redirect(groups)
#------------------------------------------------------------------------------
