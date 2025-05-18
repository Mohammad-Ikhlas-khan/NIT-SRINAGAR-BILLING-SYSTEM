from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, User

class Command(BaseCommand):
    help = "Initialize the app."

    def add_arguments(self, parser):
        parser.add_argument('--username', default=None)

    def handle(self, *args, **options):
        try:
            admin_group, _ = Group.objects.get_or_create(name='admin')
            operator_group, _ = Group.objects.get_or_create(name='operator')
            user_group, _ = Group.objects.get_or_create(name='user')

            username = options['username']
            if username:
                super_user = User.objects.get(username=username)
                super_user.groups.add(admin_group)
                super_user.save()
        except Exception as err:
            self.stdout.write("")
            if hasattr(err, '__iter__'):
                for e in err:
                    self.stdout.write(f"{err.__class__.__name__}: {str(e)}")
            else:
                self.stdout.write(f"{err.__class__.__name__}: {str(err)}")
