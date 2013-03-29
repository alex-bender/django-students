from django.core.management.base import BaseCommand, CommandError
from groups.models import Group

class Command(BaseCommand):
    args = '<group_id group_id ...>'
    help = '\n\tChose a group\n'
    
    def handle(self, *args, **options):

        if not args:
            print self.help
        for group_id in args:
            try:
                group = Group.objects.get(pk=int(group_id))
            except Group.DoesNotExist:
                raise CommandError('Group "%s" does not exist' % group_id)
            
            self.stdout.write('%s\n' % group)
