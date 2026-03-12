from datetime import datetime
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.http import Http404
from rest_framework.views import APIView
from rest_framework import status
from .models import DailyLog
from .serializers import  LogSerializer
from .selectors import LogSelectors
from macros.services import MacrosService
# Create your views here.

class LogsList(APIView):
    """
    List all logs, or create a new log.
    """
    permission_classes = [IsAuthenticated]
    def get_user(self):
        return self.request.user
        
    def get(self, request, format=None):
        logs = DailyLog.objects.filter(user=request.user)
        date = request.query_params.get("date")
        meal_type = request.query_params.get("meal_type")

        if date and meal_type:
            try:
                parsed_date = datetime.strptime(date, "%Y-%m-%d").date()
                logs = logs.filter(created_at=parsed_date, meal_type=meal_type)
                serializer = LogSerializer(logs, many=True)
                return Response(serializer.data)
            except ValueError:
                return Response(
                    {"error": "Invalid date format. Use YYYY-MM-DD."},
                    status=status.HTTP_400_BAD_REQUEST,
                )
        elif date:
            try:
                parsed_date = datetime.strptime(date, "%Y-%m-%d").date()
                data = LogSelectors.format_daily_logs(user=request.user, date=parsed_date)
                return Response(data)
            except ValueError:
                return Response(
                    {"error": "Date must be in YYYY-MM-DD format"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
        elif meal_type:
            logs = logs.filter(meal_type=meal_type)
            serializer = LogSerializer(logs, many=True)
            return Response(serializer.data)
        # DEFAULT RETURN
        serializer = LogSerializer(logs, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = LogSerializer(data=request.data, context={"request": request})
        if serializer.is_valid():
            serializer.save()
            # now every time the user add food log update their macros
            MacrosService.upsert_today_macros(self.get_user(), date=request.data['created_at'])
            return Response({"message": "Log created successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeleteLogs(APIView):
    """
    Retrieve, update or delete a log instance.
    """
    permission_classes = [IsAuthenticated]
    def get_object(self, pk):
        return get_object_or_404(DailyLog, pk=pk)
    
    def get_user(self):
        return self.request.user

    def delete(self, request, pk, date, format=None):
        log = self.get_object(pk)
        log.delete()
         # now every time the user add food log update their macros
        MacrosService.upsert_today_macros(self.get_user(), date)
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class TotalFoodLogCalculation(APIView):
    permission_classes = [IsAuthenticated]
    
    def get_user(self):
        return self.request.user
    
    def get(self, request, date, format=None):
        user = self.get_user()
        parsed_date = datetime.strptime(date, "%Y-%m-%d").date()
        data = LogSelectors.total_foods_logs(user, parsed_date)
        return Response(data, status=status.HTTP_200_OK)
    
class StreakLogs(APIView):
    permission_classes = [IsAuthenticated]

    def get_user(self):
        return self.request.user

    def get(self, request, format=None):
        user = self.get_user()
        data = LogSelectors.streak_logs(user)
        return Response({"data": data}, status=status.HTTP_200_OK)
    