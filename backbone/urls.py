from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from backbone.views import GroupList, GroupDetail  # UserList, UserDetail,

from backbone.views import StudentList, StudentDetail

urlpatterns = patterns('backbone.views',
                       url(r'^$', 'api_root'),
                       url(r'^groups/$', GroupList.as_view(),
                           name='group-list'),
                       url(r'^groups/(?P<pk>\d+)/$', GroupDetail.as_view(),
                           name='group-detail'),
                       url(r'^students/$', StudentList.as_view(),
                           name='student-list'),
                       url(r'^students/(?P<pk>\d+)/$', StudentDetail.as_view(),
                           name='student-detail'),
                       )

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'api'])
