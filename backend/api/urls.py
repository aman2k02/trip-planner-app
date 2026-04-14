from django.urls import path
from .views import plan_trip
from .views import search_location

urlpatterns = [
    path('plan-trip/', plan_trip),
    path('search-location/', search_location), 
    
]