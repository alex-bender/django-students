from django.conf.urls import patterns, include, url
from django.contrib import admin
from main.views import students, students_add,  students_edit,students_delete
from main.views import groups, groups_add, groups_edit, groups_delete
from main.views import index, logout_view
from django.contrib.auth import login


admin.autodiscover()


urlpatterns = patterns('',

    url(r'^$', 'main.views.index'),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^index/$', 'main.views.index'),
#    url(r'^login/', 'login'),
    url(r'^login/', 'main.views.olologin'),
    url(r'^logout/$', 'main.views.logout_view'),
    url(r'^new_user/$', 'main.views.CreateUserAndLogin'),

    url(r'^students/$', 'main.views.students'),
    url(r'^students_add/$', 'main.views.students_add'),
    url(r'^students_edit/(?P<student_id>\d+)/$','main.views.students_edit'),
    url(r'^students_delete/(?P<student_id>\d+)/$','main.views.students_delete'),
#------------------------------------------------------------------------------
    url(r'^groups/$', 'main.views.groups'),
    url(r'^groups_add/$', 'main.views.groups_add'),
    url(r'^groups_edit/(?P<group_id>\d+)/$','main.views.groups_edit'),
    url(r'^group_list/(?P<group_name>\w+)/$','main.views.group_list'),
    url(r'^groups_delete/(?P<group_id>\d+)/$','main.views.groups_delete'),
#------------------------------------------------------------------------------


)