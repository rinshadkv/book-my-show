from django.db import models

from localadmin.models import *

# Create your models here.

class User(models.Model):
    password=models.CharField(max_length=12)
    email=models.CharField(max_length=100)
    name=models.CharField(max_length=25,default="")
    class Meta:
        db_table='user_tb'

class Booking(models.Model):
    Movie_id=models.ForeignKey(Movies,on_delete=models.CASCADE)
    Customer=models.ForeignKey(User,on_delete=models.CASCADE)
    Movie_name=models.CharField(max_length=100)    
    Booking_date=models.CharField(max_length=120)
    Booking_time=models.CharField(max_length=20)
    Seat_category=models.CharField(max_length=20)
    Totel_seats=models.IntegerField()
    Selected_seats=models.CharField(max_length=100)
    Totel_amount=models.IntegerField()
    Payment_status=models.CharField(max_length=20)

    class Meta:
        db_table='booking_tb'