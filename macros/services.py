from django.utils import timezone
from django.contrib.auth.models import User
from users.models import UserProfile
from .models import Macros
from logs.services import FoodLogService


class MacrosService:
    
    @staticmethod
    def upsert_today_macros(user, date):
        """
        Recompute and insert/update today's macros for a user
        """
        user_profile = UserProfile.objects.get(user=user)
        macros_data = FoodLogService.get_date_macros(user, date)
        macros, created = Macros.objects.update_or_create(
            user=user_profile,
            date=date,
            defaults=macros_data
        )
        return macros
    
    @staticmethod
    def get_today_macros(user):
        today = timezone.now().date()
        user_profile = UserProfile.objects.get(user=user)

        return Macros.objects.filter(
            user=user_profile,
            date=today
        ).first()
