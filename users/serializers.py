from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    # User fields (not part of UserProfile model)
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)
    
    username_display = serializers.CharField(
        source="user.username",
        read_only=True
    )
    class Meta:
        model = UserProfile
        fields = [
            "id",
            "username",
            "password",
            "username_display",
            "name",
            "age",
            "weight",
            "height",
            "target_calories",
            "target_protein",
            "target_carbs",
            "target_fats",
        ]

    def validate(self, data):
        if not data.get("name"):
            raise serializers.ValidationError("Name is required")

        if data.get("target_calories") is not None and data["target_calories"] <= 0:
            raise serializers.ValidationError("Target calories must be greater than 0")

        return data

    def create(self, validated_data):
        # Extract user-related fields
        username = validated_data.pop("username")
        password = validated_data.pop("password")

        # Create Django User
        user = User.objects.create_user(
            username=username,
            password=password
        )

        # Create UserProfile linked to User
        profile = UserProfile.objects.create(
            user=user,
            **validated_data
        )

        return profile
