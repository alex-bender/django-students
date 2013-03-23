from django.conf import settings
from django.db import connection

from time import time
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
class TimeRenderMiddleware(object):

#------------------------------------------------------------------------------
    def process_request(self, request):
        # edit this stuff
        request.session['time_start'] = time()
        request.session['num_queries_old'] = len(connection.queries)

#------------------------------------------------------------------------------
    def process_response(self, request, response):
        
        queries = connection.queries
        query_time = 0
        query_count = 0
        
        for query in queries:
            query_time += float(query['time'])
            query_count += int(1)

        end_time = time()
        num_queries_new =  len(connection.queries)

        content = response.content
        index = content.upper().find('</BODY>')
        if index == -1:
            return response
        
        before = content[:index]
        after = content[index:]
        try:
            diff_time = end_time - request.session['time_start']
            diff_queries = num_queries_new - request.session['num_queries_old']
        except:
            diff_time = 0
            diff_queries = 0
        
        message = """<div id="query_time"></br>\n<small><center>Time to render page is: %s</br>\n
        Time to sql Query: %s</br>
        Count of queries: %s</center></small></div>""" % (diff_time, query_time, diff_queries)
        content = before + message + after
        response.content =  content
        return response
#------------------------------------------------------------------------------
