from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from main.models import LogModel

#------------------------------------------------------------------------------
class Group(models.Model):
    name = models.CharField('Name', max_length=30)
    senior = models.ForeignKey('people.Student',
                               related_name='students',
                               blank=True,
                               null=True,
                               verbose_name='Senior student')
    
    def __unicode__(self):
        return self.name



@receiver(post_save, sender=Group)
def group_post_save(sender, **kwargs):
    LogModel.objects.create(which='Group', what='Save')
    print('Group saved')
#------------------------------------------------------------------------------
@receiver(post_delete, sender=Group)
def group_post_delete(sender, **kwargs):
    LogModel.objects.create(which='Group', what='Delete')
    print('Group deleted')
#------------------------------------------------------------------------------
