from django.conf.urls import patterns, include, url
from django.contrib import admin

from main.views import HomePageView, CreteUserAndLogin
from django.core.urlresolvers import reverse_lazy

admin.autodiscover()
#import ipdb;ipdb.set_trace()
urlpatterns = patterns('',

    url(r'^$', HomePageView.as_view()),
    
    url(r"^groups/", include('groups.urls', namespace='group')),
    url(r"^students/", include('people.urls', namespace='student')),
    
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^index/$', HomePageView.as_view(), name='home'),
    url(r'^login/', 'django.contrib.auth.views.login', {'template_name': 'login.html'}, name='login'),
    
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': reverse_lazy('home')}),
    url(r'^new/user/$', CreteUserAndLogin.as_view(), name='new_user'),

)