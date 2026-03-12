from django.db import models


class Food(models.Model):
    # Basic info
    name = models.CharField(max_length=100)
    serving = models.CharField(max_length=100, blank=True)

    # ======================
    # Energy & Water
    # ======================
    calories = models.FloatField(null=True, blank=True)
    water = models.FloatField(null=True, blank=True)

    # ======================
    # Fats
    # ======================
    total_fat = models.FloatField(null=True, blank=True)
    saturated_fat = models.FloatField(null=True, blank=True)
    monounsaturated_fat = models.FloatField(null=True, blank=True)
    polyunsaturated_fat = models.FloatField(null=True, blank=True)
    trans_fat = models.FloatField(null=True, blank=True)
    cholesterol = models.FloatField(null=True, blank=True)

    # ======================
    # Carbohydrates
    # ======================
    total_carbs = models.FloatField(null=True, blank=True)
    fiber = models.FloatField(null=True, blank=True)
    sugars = models.FloatField(null=True, blank=True)
    starch = models.FloatField(null=True, blank=True)

    # ======================
    # Protein
    # ======================
    protein = models.FloatField(null=True, blank=True)

    # ======================
    # Vitamins
    # ======================
    vitamin_a = models.FloatField(null=True, blank=True)
    vitamin_c = models.FloatField(null=True, blank=True)
    vitamin_e = models.FloatField(null=True, blank=True)
    vitamin_k = models.FloatField(null=True, blank=True)

    vitamin_b1 = models.FloatField(null=True, blank=True)   # thiamin
    vitamin_b2 = models.FloatField(null=True, blank=True)   # riboflavin
    vitamin_b3 = models.FloatField(null=True, blank=True)   # niacin
    vitamin_b6 = models.FloatField(null=True, blank=True)
    vitamin_b9 = models.FloatField(null=True, blank=True)   # folate
    vitamin_b12 = models.FloatField(null=True, blank=True)

    # ======================
    # Minerals
    # ======================
    calcium = models.FloatField(null=True, blank=True)
    iron = models.FloatField(null=True, blank=True)
    magnesium = models.FloatField(null=True, blank=True)
    phosphorus = models.FloatField(null=True, blank=True)
    potassium = models.FloatField(null=True, blank=True)
    sodium = models.FloatField(null=True, blank=True)
    zinc = models.FloatField(null=True, blank=True)
    copper = models.FloatField(null=True, blank=True)
    manganese = models.FloatField(null=True, blank=True)

    # ======================
    # Meta
    # ======================
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
