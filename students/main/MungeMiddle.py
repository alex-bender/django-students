from django.conf import settings
from django import http

from time import time

class MungeForMillMiddleware(object):
    start_time = 0
    end_time = 0
    
    def process_request(self, request):
        self.start_time = time()
        pass

    def process_response(self, request, response):
        self.end_time = time()
        content = response.content
        index = content.upper().find('</BODY>')
        if index == -1: return response
        before = content[:index]
        after = content[index:]
        diff_time = self.end_time - self.start_time
        message = "</br>Time to render page is: %s" % (diff_time)
        content = before + message + after
        response.content =  content
        return response