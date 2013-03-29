from django.conf.urls import patterns, url

from groups.views import Groups, GroupList, GroupsEdit, GroupAdd, GroupDelete
from django.contrib.auth.decorators import login_required

urlpatterns = patterns('',

    url(r'^$', login_required(Groups.as_view()), name="all"),
    url(r"^add/$", login_required(GroupAdd.as_view()), name="add"),
    url(r'^edit/(?P<pk>\d+)/$', login_required(GroupsEdit.as_view()), name='edit'),
    url(r'^delete/(?P<pk>[\d]+)/$', login_required(GroupDelete.as_view()), name='delete'),
    url(r'^list/(?P<pk>[\d]+)/$', login_required(GroupList.as_view()), name='list'),


)