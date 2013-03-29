import datetime

from django.db import models
from django.utils.timezone import utc


class LogModel(models.Model):
    when = models.DateTimeField(default=datetime.datetime.utcnow().replace(tzinfo=utc))
    which = models.TextField(max_length=10)
    what = models.TextField(max_length=10)
    
    def __unicode__(self):
        return "%s %s at %s" % (self.which, self.what, self.when)
#------------------------------------------------------------------------------

