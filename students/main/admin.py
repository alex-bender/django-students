from django.contrib import admin
from main.models import Group, Student




class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'num', 'senior')
    
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_name', 'group', 'birthday_date', 'student_id_card')

admin.site.register(Student, StudentAdmin)
admin.site.register(Group, GroupAdmin)