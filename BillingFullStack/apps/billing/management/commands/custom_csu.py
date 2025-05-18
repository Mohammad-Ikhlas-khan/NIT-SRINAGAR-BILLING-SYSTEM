from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.validators import validate_email

class Command(BaseCommand):
    help = "Create superuser directly"

    def add_arguments(self, parser):
        parser.add_argument('--username', required=True)
        parser.add_argument('--email', default=None)
        parser.add_argument('--password', required=True)

    def handle(self, *args, **options):
        try:
            username = options['username']
            User.username_validator(username)
            email = options['email']
            if email:
                validate_email(email)
            password = options['password']
            validate_password(password)
            User.objects.create_superuser(username=username, email=email, password=password)
        except Exception as err:
            self.stdout.write("")
            if hasattr(err, '__iter__'):
                for e in err:
                    self.stdout.write(f"{err.__class__.__name__}: {str(e)}")
            else:
                self.stdout.write(f"{err.__class__.__name__}: {str(err)}")
            self.stdout.write("")
