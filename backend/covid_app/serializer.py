from rest_framework import serializers
from . models import My_Records
  
class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = My_Records
        
        fields ='__all__'