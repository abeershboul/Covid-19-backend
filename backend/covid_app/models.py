from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
class My_Records(models.Model):
    Country = models.CharField(max_length=30)
    Total_confarmid= models.IntegerField(default=0)
    Total_Deaths= models.IntegerField(default=0)
    Total_recovered=models.IntegerField(default=0)
    Date=models.DateTimeField(auto_now_add=False)
    class Meta:  
        db_table = "Myrecords" 

    def __str__(self):
        return self.Country

