from django.contrib import admin  
from django.urls import path  
from .views import RecordDetailView,RecordListView
urlpatterns = [  
    path('' , RecordListView.as_view() , name="list"  ),
    path('<int:pk>' , RecordDetailView.as_view() , name="detail"   ), 
]  