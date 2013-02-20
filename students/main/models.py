from django.db import models

class Group(models.Model):
    name = models.CharField(max_length=30)
    senior = models.ForeignKey('Student',related_name='senior')
    
    def __unicode__(self):
        return self.name

class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birthday_date = models.DateField()
    student_id_card = models.DecimalField(max_digits=10,decimal_places=0)
    group = models.ForeignKey('Group')

    def __unicode__(self):
        return '%s %s'%(self.first_name,self.last_name)