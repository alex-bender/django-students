from django.core.management.base import BaseCommand, CommandError
from main.models import Group

class Command(BaseCommand):
    args = '<group_id group_id ...>'
    help = 'Chose a group'
    
    def handle(self, *args, **options):
        for group_id in args:
            try:
                group = Group.objects.get(pk=int(group_id))
            except Group.DoesNotExist:
                raise CommandError('Group "%s" does not exist' % group_id)
            
            self.stdout.write('%s\n' % group)