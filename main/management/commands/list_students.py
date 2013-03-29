from django.core.management.base import BaseCommand, CommandError
from people.models import Student

class Command(BaseCommand):
    args = '<student_id student_id ...>'
    help = '\n\tChose a student\n'
    
    def handle(self, *args, **options):
        if not args:
            print self.help
        for student_id in args:
            try:
                student = Student.objects.get(pk=int(student_id))
            except Student.DoesNotExist:
                raise CommandError('Student "%s" does not exist' % student_id)
            
            self.stdout.write('%s\n' % student)