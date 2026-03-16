from rest_framework import serializers
from .models import Food
from django.contrib.auth.models import User

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = '__all__'
        read_only_fields = ["created_by"]
        
    def validate(self, data):
        if data.get('calories') < 0 or data.get('protein', 0) < 0 or data.get('carbs', 0) < 0 or data.get('fat', 0) < 0:
            raise serializers.ValidationError("Macros cannot be negative")
        return data
    
    def create(self, validated_data):
        user = self.context["request"].user
        validated_data["created_by"] = user
        return super().create(validated_data)

