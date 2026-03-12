from rest_framework import serializers
from .models import Macros
from django.contrib.auth.models import User
from users.models import UserProfile



class MacrosSerializer(serializers.ModelSerializer):
     # READ-ONLY fields (returned in response)
    # username = serializers.CharField(
    #     source="user.username",
    #     read_only=True
    # )

    # profile_name = serializers.CharField(
    #     source="user.userprofile.name",
    #     read_only=True
    # )
    
    class Meta:
        model = Macros
        fields = "__all__"

    def validate(self, data):
        if data['calories'] < 0:
            raise serializers.ValidationError("Calories cannot be negative")
        return data