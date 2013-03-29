from django.core.urlresolvers import reverse
from django import template

register = template.Library()
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
def edit_list(item):
    url = reverse('admin:%s_%s_change' % (item._meta.app_label, item._meta.module_name), args=[item.id])
    edit_link = u'<a href="{}">Edit {}</a>'.format(url,  item.__unicode__())
    return edit_link
#------------------------------------------------------------------------------
register.simple_tag(edit_list)