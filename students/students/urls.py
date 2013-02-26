from django.conf.urls import patterns, include, url
from django.contrib import admin
from main.views import show_students, show_groups
from main.editor import *
admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'students.views.home', name='home'),
    #url(r'^students/', include('students.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^group/list/$', show_groups),
    url(r'^student/list/$', show_students),
    url(r'^groups/edit/(?P<group>\w+)', edit_groups ),
    #url(r'^students/edit/', edit),
)