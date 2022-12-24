from rest_framework.generics import ListCreateAPIView , RetrieveUpdateDestroyAPIView
from .serializer import RecordSerializer
from .models import My_Records
# Create your views here.

class RecordListView(ListCreateAPIView):
    queryset=My_Records.objects.all()
    serializer_class= RecordSerializer

class RecordDetailView(RetrieveUpdateDestroyAPIView):
    queryset=My_Records.objects.all()
    serializer_class= RecordSerializer
