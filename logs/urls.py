from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    #path('', views.index, name='index'),
    path('food-logs/', views.LogsList.as_view(), name='food-logs'),
    #path('food-logs/<int:user_id>', views.LogsList.as_view(), name='food-logs'),
    path('food-logs/<int:pk>/<str:date>/', views.DeleteLogs.as_view(), name='food-logs-detail'),
    path("food-logs/<str:date>/totals/",views.TotalFoodLogCalculation.as_view(),name="food-logs-date"),
    # streaks
    path('history/streaks/', views.StreakLogs.as_view(), name='streaks'),
]

urlpatterns = format_suffix_patterns(urlpatterns)