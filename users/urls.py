from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('profile/', views.UserProfileList.as_view(), name='profile-list'),
    path('profile-details/', views.UserProfileDetail.as_view(), name='profile-details'),
    path("auth/logout/", views.LogoutView.as_view(), name="logout"),
    path("overview/", views.UserOverviewView.as_view(), name="overview"),
    path("generate-macros/", views.GenerateMacrosView.as_view(), name="generate-macros"),
    path("calculate-daily-calories/", views.GenerateDailyCaloriesView.as_view(), name="calculate-daily-calories")
]

urlpatterns = format_suffix_patterns(urlpatterns)   