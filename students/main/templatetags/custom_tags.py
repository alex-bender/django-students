from django.core.urlresolvers import reverse
from django import template

register = template.Library()
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
def edit_list(object):
    url = reverse('admin:%s_%s_change' % (object._meta.app_label, object._meta.module_name), args=[object.id])
    edit_link = u'<a href="%s">Edit %s</a>' % (url,  object.__unicode__()) 
    return edit_link
#------------------------------------------------------------------------------
register.simple_tag(edit_list)