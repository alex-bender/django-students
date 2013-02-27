from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.views.generic.simple import direct_to_template
from django.template import RequestContext

from models import Student, Group, StudentForm, GroupForm


def students(request):
    students_list = Student.objects.all().order_by('name')
    return render_to_response('students.html',
                              {'students_list': students_list,})

def students_add(request):
    # sticks in a POST or renders empty form
    form = StudentForm(request.POST or None)
    if form.is_valid():
        cmodel = form.save()
        #This is where you might chooose to do stuff.
        #cmodel.name = 'test1'
        cmodel.save()
        return redirect(students)

    return render_to_response('students_add.html',
                              {'student_form': form},
                              context_instance=RequestContext(request))    

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
def students_edit(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    
    return redirect(students)
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------

def students_delete(request, student_id):
    stud = Student.objects.get(pk=student_id).delete()

    return redirect(students)
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------





def contact_edit(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id)
    form = ContactForm(request.POST or None, instance=contact)
    if form.is_valid():
        contact = form.save()
        #this is where you might choose to do stuff.
        #contact.name = 'test'
        contact.save()
        return redirect(contacts)

    return render_to_response('contact_edit.html',
                              {'contact_form': form,
                               'contact_id': contact_id},
                              context_instance=RequestContext(request))






















#------------------------------------------------------------------------------
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------ 
def groups_list(request):
    pass
def groups_add(request, group):
    pass
def groups_edit(request, group):
    pass
def groups_delete(request, group):
    pass
