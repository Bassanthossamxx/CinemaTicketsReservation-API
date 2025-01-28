from django.http import JsonResponse
from django.shortcuts import render
from .models import *


#Function based view model and no rest framework:
def FBVModelNoRest(request):
    dataGuest = Guest.objects.all()
    #dataReservation = Reservation.objects.all()
    #dataMovie = Movie.objects.all()
    response = \
        {
        'guests': list(dataGuest.values()) ,
            #if I need to change it "practise"
        # 'movies' : list(dataMovie.values()),
        # 'reservations' : list(dataReservation.values())  ,
        }
    return JsonResponse(response)




