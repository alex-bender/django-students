from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
import datetime


#------------------------------------------------------------------------------
class Group(models.Model):
    name = models.CharField('Name', max_length=30)
    senior = models.ForeignKey('Student', related_name='student', blank=True, null=True, verbose_name='Senior student')
    
    def __unicode__(self):
        return self.name
#------------------------------------------------------------------------------
class Student(models.Model):
    name = models.CharField('Name', max_length=30)
    last_name = models.CharField('Surname',max_length=30)
    birthday_date = models.DateField()
    student_id_card = models.DecimalField('Student Id', max_digits=10, decimal_places=0)
    group = models.ForeignKey('Group')

    def __unicode__(self):
        return "%s %s" % (self.name, self.last_name)
#------------------------------------------------------------------------------
class LogModel(models.Model):
    when = models.DateTimeField(default=datetime.datetime.now)
    which = models.TextField(max_length=10)
    what = models.TextField(max_length=10)
    
    def __unicode__(self):
        return "%s %s at %s" % (self.which, self.what, self.when)
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
@receiver(post_save, sender=Student)
def student_post_save(sender, **kwargs):
    LogModel.objects.create(which='Student', what='Save')
    print('Student saved')
#------------------------------------------------------------------------------
@receiver(post_delete, sender=Student)
def student_delete(sender, **kwargs):
    LogModel.objects.create(which='Student', what='Delete')
    print('Student deleted')
#------------------------------------------------------------------------------
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
