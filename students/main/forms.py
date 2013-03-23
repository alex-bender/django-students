from django.forms import ModelForm
from main.models import Student, Group
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class StudentForm(ModelForm):
    class Meta:
        model = Student

class GroupForm(ModelForm):
    class Meta:
        model = Group

class UserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", )