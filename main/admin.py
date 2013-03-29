from django.contrib import admin

from main.models import LogModel

class LogModelAdmin(admin.ModelAdmin):
    list_display = ('which', 'when', 'what',)
    date_hierarchy = 'when'
    list_filter = ('when', 'which',)
    search_fields = ['when',]

admin.site.register(LogModel, LogModelAdmin)