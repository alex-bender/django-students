from django.core.urlresolvers import reverse
from django import template
import datetime

register = template.Library()
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
class LastNewsNode(template.Node):
    def __init__(self, format_string):
        self.format_string = format_string
                
    def render(self, context):
        return "%s %s" % (self.format_string, '')
#------------------------------------------------------------------------------
def lastnews(parser, token):
    tag_name, format_string = token.split_contents()

    return LastNewsNode(format_string[1:-1])
#------------------------------------------------------------------------------
def edit_list(object):
    url = reverse('admin:%s_%s_change' % (object._meta.app_label, object._meta.module_name), args=[object.id])
    return u'<a href="%s">Edit %s</a>' % (url,  object.__unicode__())
#------------------------------------------------------------------------------

register.simple_tag(edit_list)
register.tag('ln', lastnews)