from django.db import models
#how to write models :
#what need in tickets :
# guest  -- Movie -- Reservation
# models :
#1- for Movie
class Movie(models.Model):
    title = models.CharField(max_length=100)
    hall = models.CharField(max_length=10)
    date = models.DateField()
#2- for Guest
class Guest(models.Model):
    name = models.CharField(max_length=30)
    Phone = models.CharField(max_length=15)

#3- for Reservation

class Reservation(models.Model):
    guest = models.ForeignKey(Guest, related_name='reservation',on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, related_name='reservation' ,on_delete=models.CASCADE)
    time = models.TimeField( null=True)
    price = models.IntegerField(null=True)
    payment_method = models.CharField(max_length=20 , null=True)
