from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView

from people.models import Student


class Students(ListView):
    
    model = Student
    template_name = 'students.html'
    context_object_name = 'students'

    def get_queryset(self):
        return Student.objects.all().order_by('name')

class StudentAdd(CreateView):
    
    model = Student
    template_name = 'student_add.html'
    success_url = '/students/'

class StudentEdit(UpdateView):
    
    model = Student
    template_name = 'students_edit.html'
    success_url = '/students/'

class StudentDelete(DeleteView):
    
    model = Student
    template_name = 'item_confirm_delete.html'
    success_url = '/students/'

    def get_context_data(self, **kwargs):
        context = super(StudentDelete, self).get_context_data(**kwargs)
        context['obj'] = 'student'
        return context