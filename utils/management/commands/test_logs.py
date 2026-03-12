from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from foods.models import Food
from logs.services import FoodLogService
from django.db.models import F, Sum, FloatField
from django.db.models.functions import Coalesce

class Command(BaseCommand):
    help = "Test food log service logic" 
    def handle(self, *args, **kwargs):
        user = User.objects.get(username="gwen")
        # logs/constants.py (or inside services.py)

        # NUTRIENT_FIELDS = {
        #     # Core
        #     "calories": "calories",
        #     "protein": "protein",
        #     "carbs": "total_carbs",
        #     "fats": "total_fat",
        #     "fiber": "fiber",
        #     "sugar": "sugars",

        #     # Fats
        #     "saturated_fat": "saturated_fat",
        #     "monounsaturated_fat": "monounsaturated_fat",
        #     "polyunsaturated_fat": "polyunsaturated_fat",
        #      "trans_fat": "trans_fat",
        #     # Cholesterol & sodium
        #     "cholesterol": "cholesterol",
        #     "sodium": "sodium",
        #     # Vitamins
        #     "vitamin_a": "vitamin_a",
        #     "vitamin_c": "vitamin_c",
        #     "vitamin_e": "vitamin_e",
        #     "vitamin_k": "vitamin_k",
        #     "vitamin_b1": "vitamin_b1",
        #     "vitamin_b2": "vitamin_b2",
        #     "vitamin_b3": "vitamin_b3",
        #     "vitamin_b6": "vitamin_b6",
        #     "vitamin_b9": "vitamin_b9",
        #     "vitamin_b12": "vitamin_b12",
        #     # Minerals
        #     "calcium": "calcium",
        #     "iron": "iron",
        #     "magnesium": "magnesium",
        #     "phosphorus": "phosphorus",
        #     "potassium": "potassium",
        #     "zinc": "zinc",
        #     "copper": "copper",
        #     "manganese": "manganese",
        # }

        # # Create a new food log
        # logs = FoodLogService.get_daily_logs(user=user)

        # aggregates = {
        #     key: Coalesce(
        #         Sum(F(f"food__{field}") * F("quantity"), output_field=FloatField()),
        #         0.0
        #     )
        #     for key, field in NUTRIENT_FIELDS.items()
        # }

        # result = logs.aggregate(**aggregates)

        # self.stdout.write(str(result))