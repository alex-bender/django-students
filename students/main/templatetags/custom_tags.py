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
def do_test_request(parser, token):
    try:
        tag_name = token.split_contents() # Not really useful
    except ValueError:
        raise template.TemplateSyntaxError("%r error" % token.contents.split()[0])
    print 1
    return RequestTestNode()
#------------------------------------------------------------------------------
class RequestTestNode(template.Node):
    def __init__(self):
        self.request = template.Variable('request')
        print template.Variable('settings')

        
    def render(self, context):
        
        print context['settings'].SITE_ID
        
        #rqst = self.request.resolve(context)
        return "%s" % ''
#------------------------------------------------------------------------------

register.tag('test_request', do_test_request)
register.tag('ln', lastnews)
