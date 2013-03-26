from django.conf.urls import patterns, include, url
from django.contrib import admin

from main.views import students_edit, students_delete
from main.views import logout_view
from main.views import HomePageView, CreteUserAndLogin, Students, StudentAdd
from main.views import Groups, GroupList, GroupsEdit, GroupAdd, GroupDelete
 


admin.autodiscover()


urlpatterns = patterns('',

    url(r'^$', HomePageView.as_view()),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^index/$', HomePageView.as_view(), name='home'),
    url(r'^login/', 'django.contrib.auth.views.login', {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', 'main.views.logout_view', name='logout'),
    url(r'^new/user/$', CreteUserAndLogin.as_view(), name='new_user'),

    
    url(r'^students/$', Students.as_view(), name='students'),
    url(r'^new/student/$', StudentAdd.as_view(), name='new_student'),
    url(r'^edit/students/(?P<student_id>\d+)/$', 'main.views.students_edit', name='edit_students'),
    url(r'^delete/student/(?P<student_id>\d+)/$', 'main.views.students_delete', name='delete_students'),
#------------------------------------------------------------------------------
    
    url(r'^groups/$', Groups.as_view(), name='groups'),
    url(r'^new/group/$', GroupAdd.as_view(), name='new_group'),
    url(r'^edit/groups/(?P<group_id>\d+)/$', GroupsEdit.as_view(), name='edit_groups'),
    url(r'^delete/group/(?P<group_id>\d+)/$', GroupDelete.as_view(), name='delete_grous'),
    
    url(r'^list/group/(?P<group_name>\w+)/$', GroupList.as_view(), name='list_grups'),
#------------------------------------------------------------------------------


)