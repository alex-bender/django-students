from django.conf.urls import patterns, include, url
from django.contrib import admin
from main.views import students, students_add,  students_edit,students_delete
from main.views import groups, groups_add, groups_edit, groups_delete
from main.views import  auth_user, post#, new_user,

admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'students.views.home', name='home'),
    #url(r'^students/', include('students.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^auth/(?P<username>\w+)/(?P<password>\w+)/', 'main.views.auth_user'),
    url(r'^new_user/$', 'main.views.CreateUserAndLogin'),

    url(r'^students/$', 'main.views.students'),
    url(r'^students_add/$', 'main.views.students_add'),
    url(r'^students_edit/(?P<student_id>\d+)/$','main.views.students_edit'),
    url(r'^students_delete/(?P<student_id>\d+)/$','main.views.students_delete'),
#------------------------------------------------------------------------------
    url(r'^groups/$', 'main.views.groups'),
    url(r'^groups_add/$', 'main.views.groups_add'),
    url(r'^groups_edit/(?P<group_id>\d+)/$','main.views.groups_edit'),
    url(r'^groups_delete/(?P<group_id>\d+)/$','main.views.groups_delete'),
#------------------------------------------------------------------------------
    url(r'^registration/$', 'main.views.new_user'),
    

)