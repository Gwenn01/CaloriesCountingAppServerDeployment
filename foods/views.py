from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Food
from .serializers import FoodSerializer

# Create your views here.
class FoodList(APIView):
    
    def get(self, request):
        foods = Food.objects.all()
        serializer = FoodSerializer(foods, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = FoodSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Food created successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class FoodDetail(APIView):
    def get_object(self, pk):
        return get_object_or_404(Food, pk=pk)

    def get(self, request, pk):
        food = self.get_object(pk)
        serializer = FoodSerializer(food)
        return Response(serializer.data)
    
    def put(self, request, pk):
        food = self.get_object(pk)
        serializer = FoodSerializer(food, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Food updated successfully"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        food = self.get_object(pk)
        food.delete()
        return Response({"message": "Food deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
    