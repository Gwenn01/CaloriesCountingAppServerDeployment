import json
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny
from django.shortcuts import get_object_or_404 
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render
from rest_framework.authtoken.models import Token
from .models import UserProfile
from .serializers import UserProfileSerializer
from .services import UserProfileService

# Create your views here.
class UserProfileList(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        user_profile = UserProfile.objects.all()
        serializer = UserProfileSerializer(user_profile, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "message": "User profile saved successfully",
                    "data": serializer.data,
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UserProfileDetail(APIView):
    permission_classes = [IsAuthenticated]
    def get_object(self):
        return get_object_or_404(
            UserProfile,
            user=self.request.user
        )

    def get(self, request):
        user_profile = self.get_object()
        serializer = UserProfileSerializer(user_profile)
        return Response(serializer.data)

    def put(self, request): 
        user_profile = self.get_object()
        serializer = UserProfileSerializer(user_profile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"Message": "User updated successfully", "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        user_profile = self.get_object()
        user_profile.delete()
        return Response({"Message": "User deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
    
        
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # Delete the user's token
        Token.objects.filter(user=request.user).delete()
        return Response(
            {"message": "Logged out successfully"},
            status=status.HTTP_200_OK
        )
  
        
class UserOverviewView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        data = UserProfileService.calculate_remaining_macros(request.user)
        return Response(data, status=status.HTTP_200_OK)
    
    
class GenerateMacrosView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        total_calories = request.data.get('total_calories')
        data = UserProfileService.generate_macros_base_calories(total_calories)
        return Response(data, status=status.HTTP_200_OK)
    
    
class GenerateDailyCaloriesView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        data = request.data
        daily_calories = UserProfileService.calculate_daily_calories(
            data['age'], data['weight'], data['height'], data['gender'], data['activity_level'], data['goal'])
        return Response({'daily_calories': daily_calories}, status=status.HTTP_200_OK)