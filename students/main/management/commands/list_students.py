from django.core.management.base import BaseCommand, CommandError
from main.models import Student

class Command(BaseCommand):
    args = '<student_id student_id ...>'
    help = 'Chose a students'
    
    def handle(self, *args, **options):
        for student_id in args:
            try:
                student = Student.objects.get(pk=int(student_id))
            except Student.DoesNotExist:
                raise CommandError('Student "%s" does not exist' % student)
            
            self.stdout.write('%s\n' % student)