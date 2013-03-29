from django.forms import ModelForm

from people.models import Student

class StudentForm(ModelForm):
    class Meta:
        model = Student