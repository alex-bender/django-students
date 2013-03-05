from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender='Student')
def my_callback(sender, **kwargs):
    print('Request complite. Student changed 0r added')

    
class Group(models.Model):
    name = models.CharField('Name', max_length=30)
    num = models.DecimalField('Amt.', max_digits=2, decimal_places=0)
    senior = models.ForeignKey('Student', related_name='student', blank=True, null=True, verbose_name='Senior student')
    
    def __unicode__(self):
        return self.name

class Student(models.Model):
    name = models.CharField('Name', max_length=30)
    last_name = models.CharField('Surname',max_length=30)
    birthday_date = models.DateField()
    student_id_card = models.DecimalField('Student Id', max_digits=10, decimal_places=0)
    group = models.ForeignKey('Group')

    def __unicode__(self):
        return "%s %s" % (self.name, self.last_name)

