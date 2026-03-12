from django.db.models import F, Sum, FloatField
from django.db.models.functions import Coalesce
from .models import DailyLog
from .serializers import LogSerializer

class FoodLogService:
    
    @staticmethod
    def get_date_logs(user, date):
        log =  DailyLog.objects.filter(
            user=user,
            created_at=date
        )
        return log
    # calculate the food nutrition base on the data log of user
    @staticmethod
    def get_date_macros(user, date):
        logs = FoodLogService.get_date_logs(user=user, date=date)

        NUTRIENT_FIELDS = {
            # Core
            "calories": "calories",
            "protein": "protein",
            "carbs": "total_carbs",
            "fats": "total_fat",
            "fiber": "fiber",
            "sugar": "sugars",

            # Fats
            "saturated_fat": "saturated_fat",
            "monounsaturated_fat": "monounsaturated_fat",
            "polyunsaturated_fat": "polyunsaturated_fat",
            "trans_fat": "trans_fat",
            # Cholesterol & sodium
            "cholesterol": "cholesterol",
            "sodium": "sodium",
            # Vitamins
            "vitamin_a": "vitamin_a",
            "vitamin_c": "vitamin_c",
            "vitamin_e": "vitamin_e",
            "vitamin_k": "vitamin_k",
            "vitamin_b1": "vitamin_b1",
            "vitamin_b2": "vitamin_b2",
            "vitamin_b3": "vitamin_b3",
            "vitamin_b6": "vitamin_b6",
            "vitamin_b9": "vitamin_b9",
            "vitamin_b12": "vitamin_b12",
            # Minerals
            "calcium": "calcium",
            "iron": "iron",
            "magnesium": "magnesium",
            "phosphorus": "phosphorus",
            "potassium": "potassium",
            "zinc": "zinc",
            "copper": "copper",
            "manganese": "manganese",
        }

        aggregates = {
            key: Coalesce(
                Sum(F(f"food__{field}") * F("quantity"), output_field=FloatField()),
                0.0
            )
            for key, field in NUTRIENT_FIELDS.items()
        }

        result = logs.aggregate(**aggregates)
        return  result
    
    
    
