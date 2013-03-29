from django.forms import ModelForm

from groups.models import Group

class GroupForm(ModelForm):
    class Meta:
        model = Group