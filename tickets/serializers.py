from .models import *
from rest_framework import serializers

class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = ['id', 'name', 'Phone', 'reservation']

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model=Movie
        fields='__all__'

class ReservationSerializer(serializers.ModelSerializer):
    #choosen needed fields to endpoint it
    guest_name = serializers.CharField(source='guest.name', read_only=False)
    movie_title = serializers.CharField(source='movie.title', read_only=False)
    class Meta:
        model = Reservation
        fields = ['id', 'guest_name', 'movie_title']






