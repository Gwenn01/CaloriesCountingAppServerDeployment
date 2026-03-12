from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from users.services import UserProfileService

class Command(BaseCommand):
    help = "Test user service logic"
    def handle(self, *args, **kwargs):
        ...
        user = User.objects.get(username='gwen')
        macros = UserProfileService.calculate_remaining_macros(user)
        
        self.stdout.write(str(macros))