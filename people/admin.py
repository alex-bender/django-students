from django.contrib import admin

from people.models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_name', 'group', 'birthday_date', 'student_id_card',)
    date_hierarchy = 'birthday_date'
    list_filter = ('name', 'group', 'birthday_date', 'student_id_card',)
    search_fields = ['name', 'last_name', 'birthday_date', 'student_id_card',]

admin.site.register(Student, StudentAdmin)