from django.contrib import admin

from groups.models import Group

class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'senior',)
    list_filter = ('name',)
    search_fields = ['name', 'senior',]

admin.site.register(Group, GroupAdmin)
