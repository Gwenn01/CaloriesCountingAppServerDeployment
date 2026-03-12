from rest_framework import serializers
from .models import Food

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = '__all__'
        
    def validate(self, data):
        if data.get('calories') < 0 or data.get('protein', 0) < 0 or data.get('carbs', 0) < 0 or data.get('fat', 0) < 0:
            raise serializers.ValidationError("Macros cannot be negative")
        return data

