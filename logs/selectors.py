from django.shortcuts import get_object_or_404
from django.utils import timezone
from datetime import timedelta
from .models import DailyLog
from .serializers import LogSerializer
from users.models import UserProfile

class LogSelectors:
    ...
    
    @staticmethod
    def format_daily_logs(user, date):
        logs = (
            DailyLog.objects
            .filter(user=user, created_at=date)
            .select_related("food")   
            .order_by("created_at")
        )

        data = {
            "date": date,
            "breakfast": [],
            "lunch": [],
            "dinner": [],
            "snacks": [],
        }

        for log in logs:
            data[log.meal_type].append(LogSerializer(log).data)
        
        return data
    
    @staticmethod
    def total_foods_logs(user, date):
        data = {
            "goal_calories": 0,
            "food_calories": 0,
            "remaining": 0,
            "breakfast_calories": 0,
            "lunch_calories": 0,
            "dinner_calories": 0,
            "snack_calories": 0,
        }
        user_profile = get_object_or_404(UserProfile, user=user)
        logs = (
            DailyLog.objects
            .filter(user=user, created_at=date)
            .select_related("food")
        )
        for log in logs:
            calories = log.food.calories * log.quantity
            data[f"{log.meal_type}_calories"] += calories
            data["food_calories"] += calories

        data["goal_calories"] = user_profile.target_calories
        data["remaining"] = data["goal_calories"] - data["food_calories"]
        return data
    
    @staticmethod
    def streak_logs(user):
        today = timezone.now().date()
        streak = 0
        current_day = today
        while True:
            has_log = DailyLog.objects.filter(
                user=user,
                created_at=current_day
            ).exists()
            if not has_log:
                break
            streak += 1
            current_day -= timedelta(days=1)
        return streak