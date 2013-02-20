from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

from main.views import group_list

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'students.views.home', name='home'),
    #url(r'^students/', include('students.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^group/list/', group_list),
)