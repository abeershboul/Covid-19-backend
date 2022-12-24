from django.contrib import admin
from django.urls import path 
from .views import Homepage,get_Country_info,Summary
urlpatterns = [
    path('' , Homepage , name='home' ),
    path('date/' , get_Country_info , name='country_info' ),
    path('summary/' , Summary , name='summary' ),
]
