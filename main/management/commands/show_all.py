from django.core.management.base import BaseCommand
from main.models import Student, Group

class Command(BaseCommand):
    args = ''
    help = 'Show students & groups list'
    
    def handle(self, *args, **options):
        students = Student.objects.all()           
        groups = Group.objects.all()
    
    
        self.stdout.write('%s\n' % students)
        self.stdout.write('%s\n' % groups)