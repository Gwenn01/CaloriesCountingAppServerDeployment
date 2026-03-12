from django.test import TestCase
from django.contrib.auth.models import User
from foods.models import Food
from django.utils import timezone

from .models import DailyLog
from .services import FoodLogService


class FoodLogServiceTest(TestCase):

    def setUp(self):
        # ✅ You MUST create the user here
        self.user = User.objects.create_user(
            username="testuser",
            password="password123"
        )

        self.food = Food.objects.create(
            name="Rice",
            calories=130,
            protein=2.7,
            total_carbs=28,
            total_fat=0.3
        )

        DailyLog.objects.create(
            user=self.user,
            food=self.food,
            meal_type="Lunch",
            quantity=2,
            created_at=timezone.now().date()
        )

    def test_user_exists(self):
        users = User.objects.all()
        print(users)  # <QuerySet [<User: testuser>]>
        self.assertEqual(users.count(), 1)

    def test_daily_macros(self):
        macros = FoodLogService.get_daily_macros(self.user)
        print(macros)
        self.assertIsNotNone(macros["total_calories"])

