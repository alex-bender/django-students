from django import forms

from django.forms import ModelForm
from main.models import Student, Group
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class StudentForm(ModelForm):
    class Meta:
        model = Student

class GroupForm(ModelForm):
    class Meta:
        model = Group

#class UserForm(UserCreationForm):
#    firstname = forms.CharField(max_length=30, required=False)
#    lastname = forms.CharField(max_length=30, required=False)
#    email = forms.CharField(max_length=30)

class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email")

class LoginForm(AuthenticationForm):
    username = forms.CharField(required=True)
    password = forms.PasswordInput()
    
    class Meta:
        model = User
        fields = ("username", "password")
