from django.shortcuts import render
from django.http import JsonResponse
import requests

# Create your views here.

def Homepage(request):

    URL = "https://api.covid19api.com/world/total"
    r = requests.get(url = URL)    
    result = r.json()    
    return JsonResponse(result)


def Summary(request):

    URL = "https://api.covid19api.com/summary"
    r = requests.get(url = URL)    
    data = r.json() 
    return JsonResponse(data['Countries'] , safe=False)    

def get_Country_info(request):
    
    country_info = request.GET['country']
    from_date =  request.GET['from']
    to = request.GET['to']
    PARAMS = {
        "from" : from_date,
        "to": to,  
    }
    URL = f"https://api.covid19api.com/country/{country_info}/status/confirmed"
    r = requests.get(url = URL , params= PARAMS)    
    result = r.json()   
    return JsonResponse(result , safe=False)    
