from django.conf.urls import patterns, include, url
from django.contrib import admin
from main.views import *

admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'students.views.home', name='home'),
    #url(r'^students/', include('students.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
#-------------------------------------------------------------------------------    
    url(r'^students/$', 'main.views.students'),
    url(r'^students_add/$', 'main.views.students_add'),
    url(r'^students_edit/(?P<student_id>\d+)/$','main.views.students_edit'),
    url(r'^students_delete/(?P<student_id>\d+)/$','main.views.students_delete'),
    
#-------------------------------------------------------------------------------
    url(r'^contact_add/$', 'main.views.contact_add'),
    url(r'^contact_edit/(?P<contact_id>\d+)/$','main.views.contact_edit'),
    url(r'^contact_delete/(?P<contact_id>\d+)/$','main.views.contact_delete'),
)