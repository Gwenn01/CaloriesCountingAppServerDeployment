# users/services.py
from django.shortcuts import get_object_or_404
from .models import UserProfile
from macros.services import MacrosService

class UserProfileService:
    #get the user profile
    @staticmethod
    def get_user_profile(user):
        return get_object_or_404(UserProfile, user=user)
    
    # calculate the data in the overview
    @staticmethod
    def calculate_remaining_macros(user):
        profile = UserProfileService.get_user_profile(user)
        daily_macros = MacrosService.get_today_macros(user)

        calories = daily_macros.calories if daily_macros else 0
        protein = daily_macros.protein if daily_macros else 0
        carbs = daily_macros.carbs if daily_macros else 0
        fats = daily_macros.fats if daily_macros else 0

        return {
            "calories_goal": int(profile.target_calories),
            "current_calories": int(calories),
            "calories_remaining": int(profile.target_calories - calories),

            "protein_goal": int(profile.target_protein),
            "current_protein": int(protein),
            "protein_remaining": int(profile.target_protein - protein),

            "carbs_goal": int(profile.target_carbs),
            "current_carbs": int(carbs),
            "carbs_remaining": int(profile.target_carbs - carbs),

            "fats_goal": int(profile.target_fats),
            "current_fats": int(fats),
            "fats_remaining": int(profile.target_fats - fats),
        }
    
    # generate macros base on calories
    @staticmethod
    def generate_macros_base_calories(total_calories):
        macros_percent = {
            "protein": 0.30,
            "carbs": 0.40,
            "fat": 0.30
        }

        protein_grams = (total_calories * macros_percent["protein"]) / 4
        carbs_grams = (total_calories * macros_percent["carbs"]) / 4
        fat_grams = (total_calories * macros_percent["fat"]) / 9

        return {
            "protein_g": round(protein_grams),
            "carbs_g": round(carbs_grams),
            "fat_g": round(fat_grams)
        }
    
    # calculate the calories
    @staticmethod
    def calculate_bmr(weight, height, age, gender):
        if gender == "male":
            return 10 * weight + 6.25 * height - 5 * age + 5
        else:  # female
            return 10 * weight + 6.25 * height - 5 * age - 161
            
    @staticmethod
    def calculate_daily_calories(age, weight, height, gender, activity_level, goal):
        ACTIVITY_MULTIPLIER = {
            "sedentary": 1.2,
            "light": 1.375,
            "moderate": 1.55,
            "active": 1.725,
            "athlete": 1.9,
        }
        bmr = UserProfileService.calculate_bmr(weight, height, age, gender)
        activity_multiplier = ACTIVITY_MULTIPLIER[activity_level]

        if goal == "loss":
            daily_calories = bmr * activity_multiplier * 0.8
        elif goal == "gain":
            daily_calories = bmr * activity_multiplier * 1.2
        else:
            daily_calories = bmr * activity_multiplier

        return daily_calories


        