from django.contrib import admin
from main.models import Group, Student, LogModel


class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'senior',)
    list_filter = ('name',)
    search_fields = ['name', 'senior',]
    
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_name', 'group', 'birthday_date', 'student_id_card',)
    date_hierarchy = 'birthday_date'
    list_filter = ('name', 'group', 'birthday_date', 'student_id_card',)
    search_fields = ['name', 'last_name', 'birthday_date', 'student_id_card',]
    
class LogModelAdmin(admin.ModelAdmin):
    list_display = ('which', 'when', 'what',)
    date_hierarchy = 'when'
    list_filter = ('when', 'which',)
    search_fields = ['when',]

admin.site.register(Student, StudentAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(LogModel, LogModelAdmin)