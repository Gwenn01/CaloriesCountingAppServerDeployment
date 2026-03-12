from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    #path('', views.index, name='index'),
    path('macros/', views.MacrosList.as_view(), name='macros-list'),
    path('macros/<int:pk>', views.MacrosDetail.as_view(), name='macros-details'),
]

urlpatterns = format_suffix_patterns(urlpatterns)