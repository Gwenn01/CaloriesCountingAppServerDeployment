from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    #path('', views.index, name='index'),
    path('foods/', views.FoodList.as_view(), name='foods-list'),
    path('foods/<int:pk>/', views.FoodDetail.as_view(), name='food-details'),
]

urlpatterns = format_suffix_patterns(urlpatterns)