from .models import *
from rest_framework import serializers

class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model=Guest
        fields='__all__'

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model=Movie
        fields='__all__'

class ReservationSerializer(serializers.ModelSerializer):
    #choosen needed fields to endpoint it
    class Meta:
        model = Reservation
        fields = ['id', 'guest', 'movie']






