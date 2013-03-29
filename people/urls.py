from django.conf.urls import patterns, url

from people.views import Students, StudentAdd, StudentDelete, StudentEdit
from django.contrib.auth.decorators import login_required

urlpatterns = patterns('',

    url(r'^$', login_required(Students.as_view()), name='all'),
    url(r'^new/$', login_required(StudentAdd.as_view()), name='add'),
    url(r'^edit/(?P<pk>\d+)/$', login_required(StudentEdit.as_view()), name='edit'),
    url(r'^delete/(?P<pk>\d+)/$', login_required(StudentDelete.as_view()), name='delete'),



)