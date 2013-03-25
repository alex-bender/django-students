from django.conf.urls import patterns, include, url
from django.contrib import admin
from main.views import students, students_add,  students_edit,students_delete
from main.views import groups, groups_add, groups_edit, groups_delete
from main.views import index, logout_view


admin.autodiscover()


urlpatterns = patterns('',

    url(r'^$', 'main.views.index'),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^index/$', 'main.views.index'),
    url(r'^login/', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    url(r'^logout/$', 'main.views.logout_view'),
    url(r'^new/user/$', 'main.views.create_user_and_login'),

    url(r'^students/$', 'main.views.students'),
    url(r'^new/students/$', 'main.views.students_add'),
    url(r'^edit/students/(?P<student_id>\d+)/$','main.views.students_edit'),
    url(r'^delete/students/(?P<student_id>\d+)/$','main.views.students_delete'),
#------------------------------------------------------------------------------
    url(r'^groups/$', 'main.views.groups'),
    url(r'^add/groups/$', 'main.views.groups_add'),
    url(r'^edit/groups/(?P<group_id>\d+)/$','main.views.groups_edit'),
    url(r'^delete/groups/(?P<group_id>\d+)/$','main.views.groups_delete'),
    url(r'^list/group/(?P<group_name>\w+)/$','main.views.group_list'),
#------------------------------------------------------------------------------


)