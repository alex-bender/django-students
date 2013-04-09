from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from main.models import LogModel

#------------------------------------------------------------------------------
class Student(models.Model):
    name = models.CharField('Name', max_length=30)
    last_name = models.CharField('Surname', max_length=30)
    birthday_date = models.DateField()
    student_id_card = models.DecimalField('Student Id', max_digits=10,
                                          decimal_places=0)
    group = models.ForeignKey('groups.Group', related_name='groups')
    

    def __unicode__(self):
        return "%s %s" % (self.name, self.last_name)
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