from django.contrib import admin
from django.urls import path
from fishdb import views

urlpatterns = [
    path('api/fish/', views.FishListCreateAPIView.as_view(), name='fish-list-create'),
    path('api/fish/<str:PIT_code>/', views.FishDetailAPIView.as_view(), name='fish-detail'),
    
    # URL patterns for FishPos table
    path('api/fishpositions/<str:AT_code>/', views.FishPositionbyATCodeAPI.as_view(), name='fishpositions-by-at-code'),
]
