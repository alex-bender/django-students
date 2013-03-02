from django.db import models


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

