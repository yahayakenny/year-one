from django.urls import path
from meal_app import views

urlpatterns = [
    path('meals/', views.get_meals, name = "get_meals"),
    path('meals/<int:id>/',views.meal_detail, name = "meal_detail"),
    
]