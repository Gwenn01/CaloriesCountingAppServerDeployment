# macros/models.py
from django.db import models
from users.models import UserProfile
from logs.models import  DailyLog
from django.utils import timezone

class Macros(models.Model):
    user = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
        related_name="macros"
    )

    # Core macros
    calories = models.FloatField(default=0)
    protein = models.FloatField(default=0)
    carbs = models.FloatField(default=0)
    fats = models.FloatField(default=0)
    fiber = models.FloatField(default=0)
    sugar = models.FloatField(default=0)

    # Fats breakdown
    saturated_fat = models.FloatField(default=0)
    monounsaturated_fat = models.FloatField(default=0)
    polyunsaturated_fat = models.FloatField(default=0)
    trans_fat = models.FloatField(default=0)

    # Cholesterol & sodium
    cholesterol = models.FloatField(default=0)
    sodium = models.FloatField(default=0)

    # Vitamins
    vitamin_a = models.FloatField(default=0)
    vitamin_c = models.FloatField(default=0)
    vitamin_d = models.FloatField(default=0)
    vitamin_e = models.FloatField(default=0)
    vitamin_k = models.FloatField(default=0)
    vitamin_b1 = models.FloatField(default=0)
    vitamin_b2 = models.FloatField(default=0)
    vitamin_b3 = models.FloatField(default=0)
    vitamin_b6 = models.FloatField(default=0)
    vitamin_b9 = models.FloatField(default=0)
    vitamin_b12 = models.FloatField(default=0)

    # Minerals
    calcium = models.FloatField(default=0)
    iron = models.FloatField(default=0)
    magnesium = models.FloatField(default=0)
    phosphorus = models.FloatField(default=0)
    potassium = models.FloatField(default=0)
    zinc = models.FloatField(default=0)
    copper = models.FloatField(default=0)
    manganese = models.FloatField(default=0)

    # Day tracking
    date = models.DateField(default=timezone.now)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'date')
