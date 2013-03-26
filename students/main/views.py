from django.views.generic.base import TemplateView, View
from django.views.generic.edit import FormView, CreateView, DeleteView
from django.views.generic import ListView

from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, redirect, get_object_or_404, render
from django.template import RequestContext

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from forms import StudentForm, GroupForm, UserCreateForm
from models import Student, Group


#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
class HomePageView(TemplateView):
    template_name = "base.html"
    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        return context

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/index/')

class CreteUserAndLogin(View):
    form_class = UserCreateForm
    initial = {}
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

            return HttpResponseRedirect('/index/')

        return render(request, self.template_name, {'form': form})

class Students(ListView):
    model = Student
    template_name = 'students.html'
    context_object_name = 'students'
    
    def get_queryset(self):
        return Student.objects.all().order_by('name')

class StudentAdd(CreateView):
    form_class = StudentForm
    template_name = 'student_add.html'
    success_url = '/students/'

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

@login_required
def students_delete(request, student_id):
    Student.objects.get(pk=student_id).delete()

    return redirect(students)

class Groups(ListView):
    model = Group
    template_name = 'groups.html'
    context_object_name = 'groups'

    def get_queryset(self):
        return Group.objects.order_by('pk')

class GroupAdd(CreateView):
    form_class = GroupForm
    template_name = 'group_add.html'
    success_url = '/groups/'

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
class GroupsEdit(FormView):
    
    form_class = GroupForm
    initial = {}
    template_name = 'students_in_group.html'

class GroupList(ListView):
    model = Student
    template_name = 'students_in_group.html'
    context_object_name = 'students_list'
    
    def get_queryset(self):
        group_name = self.kwargs.get('group_name')
        print group_name
        return self.model.objects.filter(group__name=group_name)

@login_required
def groups_delete(request, group_id):
    Group.objects.get(pk=group_id).delete()
    
    return redirect(groups)

class GroupDelete(DeleteView):

# def get
# def post ????

    model = Group
    template_name = 'item_confirm_delete.html'
    success_url = '/groups/'

