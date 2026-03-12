from rest_framework import serializers
from .models import DailyLog
from foods.serializers import FoodSerializer
from foods.models import Food

class LogSerializer(serializers.ModelSerializer):
    # init the user
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    
    food = serializers.PrimaryKeyRelatedField(
        queryset=Food.objects.all(),
        write_only=True
    )
    food_details = FoodSerializer(source="food", read_only=True)
    username = serializers.CharField(source="user.username", read_only=True)
    class Meta:
        model = DailyLog
        fields = '__all__'
        
    def validate(self, data):
        quantity = data.get("quantity")
        food = data.get("food")

        if quantity is not None and quantity <= 0:
            raise serializers.ValidationError({
                "quantity": "Quantity must be greater than 0."
            })

        if food and food.calories < 0:
            raise serializers.ValidationError({
                "food": "Food calories cannot be negative."
            })

        return data
