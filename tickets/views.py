from http.client import responses

from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import GuestSerializer, MovieSerializer, ReservationSerializer


def FBV_Model_No_Rest(request):
    guest = Guest.objects.all()
    response = {
        'guests': list(guest.values()),
    }
    return JsonResponse(response)

#1- GET / POST For Guest
@api_view(['GET', 'POST'])
def FBV_List_Guest(request):
    if request.method == 'GET':
        guests = Guest.objects.all()
        serializer = GuestSerializer(guests, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = GuestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#2- GET / POST For Movies
@api_view(['GET','POST'])
def FBV_List_Movie(request):
    if request.method == 'GET':
        movie = Movie.objects.all()
        serializer = MovieSerializer(movie, many = True)
        return Response(serializer.data , status = status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status = status.HTTP_200_OK)
        return Response(serializer.errors , status = status.HTTP_400_BAD_REQUEST)


#3- GET / POST For Reservation
@api_view(['GET', 'POST'])
def FBV_List_Reservation(request):
    if request.method == 'GET':
        reservations = Reservation.objects.all()
        serializer = ReservationSerializer(reservations, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = ReservationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#4- GET "PK" / PUT / DELETE For Guest
@api_view(['GET', 'PUT', 'DELETE'])
def FBV_PK_Guest(request, pk):
    try:
        guest = Guest.objects.get(pk=pk)
    except Guest.DoesNotExist:
        return Response({"error": "Guest not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = GuestSerializer(guest)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = GuestSerializer(guest, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        guest.delete()
        guests = Guest.objects.all()
        serializer = GuestSerializer(guests, many=True)
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)


#5- GET "PK" / PUT / DELETE For Movie
@api_view(['GET', 'PUT', 'DELETE'])
def FBV_PK_Movie(request,pk):
    try:
       movie = Movie.objects.get(pk=pk)
    except Movie.DoesNotExist:
       return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = MovieSerializer(movie)
        return Response(serializer.data ,status = status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = MovieSerializer(movie, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors , status = status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        movie.delete()
        return Response({"message":"Movie Has Been Deleted"} , status = status.HTTP_200_OK)

#6- GET "PK" / PUT / DELETE For Reservation
@api_view(['GET', 'PUT', 'DELETE'])
def FBV_PK_Reservation(request,pk):
    try:
       reservation = Reservation.objects.get(pk=pk)
    except Reservation.DoesNotExist:
       return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ReservationSerializer(reservation)
        return Response(serializer.data ,status = status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = ReservationSerializer(reservation, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors , status = status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        reservation.delete()
        return Response({"message":"reservation Has Been Deleted"} , status = status.HTTP_200_OK)
