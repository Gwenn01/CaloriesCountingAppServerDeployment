from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from foods.models import Food

class DailyLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    meal_type = models.CharField(max_length=50)
    quantity = models.IntegerField(default=1)
    created_at = models.DateField(default=timezone.now)

    def total_calories(self):
        return (self.food.calories or 0) * self.quantity

    def __str__(self):
        return f"{self.user.username} - {self.food.name}"
