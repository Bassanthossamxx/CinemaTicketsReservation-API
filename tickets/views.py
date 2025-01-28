from django.http import JsonResponse
from django.shortcuts import render
from .models import *


#Function based view model and no rest framework:
def FBVModelNoRest(request):
    data = Guest.objects.all()
    response = \
        {
        'guests': list(data.values())  # Convert to list
        }
    return JsonResponse(response)




