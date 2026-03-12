from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from users.services import UserProfileService
from .models import Macros
from .serializers import MacrosSerializer
# Create your views here.

class MacrosList(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        #get macros base on the user only
        profile = UserProfileService.get_user_profile(request.user)
        macros = Macros.objects.filter(user=profile)
        serializer = MacrosSerializer(macros, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = MacrosSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MacrosDetail(APIView):
    def get_object(self, pk):
        try:
            return Macros.objects.get(pk=pk)
        except Macros.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        macros = self.get_object(pk)
        serializer = MacrosSerializer(macros)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        macros = self.get_object(pk)
        serializer = MacrosSerializer(macros, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
    
    def delete(self, request, pk):
        macros = self.get_object(pk)
        macros.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)