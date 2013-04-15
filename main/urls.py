from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.decorators.csrf import csrf_exempt

from main.views import HomePageView, CreteUserAndLogin, AjaxView
from django.core.urlresolvers import reverse_lazy

admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$', csrf_exempt(HomePageView.as_view()), name='home'),
    
    url(r"^groups/", include('groups.urls', namespace='group')),
    url(r"^students/", include('people.urls', namespace='student')),
    url(r"^api/", include('backbone.urls')),


    url(r"^aj/", csrf_exempt(AjaxView.as_view())),

    
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^login/', 'django.contrib.auth.views.login',
        {'template_name': 'login.html'}, name='login'),
    
    url(r'^logout/$', 'django.contrib.auth.views.logout',
        {'next_page': reverse_lazy('home')}),
    url(r'^new/user/$', CreteUserAndLogin.as_view(), name='new_user'),


)