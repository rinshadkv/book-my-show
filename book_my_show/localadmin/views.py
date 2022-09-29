from django.shortcuts import render,redirect

from user.models import Booking, User
from .models import *

# Create your views here.
def AdminLogin(request):

    msg=''
    if request.method=='POST':
        email=request.POST["username"]  
        password=request.POST["password"]    
        admin_email="admin"
        admin_password="12345678"
        if(email==admin_email)and(password==admin_password):
            return redirect("admin-dashboard")
        else:
           msg="password or username incorrect"      
    return render(request,"admin-login.html",{"msg":msg})


def AddMovie(request):
    if request.method=="POST":
        Movie_name=request.POST["movie-name"]
        Release_date=request.POST["release-date"]
        Movie_poster=request.FILES["movie-poster"]
        Languages=request.POST["languages"]
        Gener=request.POST["movie-gener"]
        About_movie=request.POST["about-movie"]
        Movie_trailor=request.POST["trailor"]
        Movie_duration=request.POST["movie-duration"]
        obj=Movies(Movie_name=Movie_name,Release_date=Release_date,Movie_poster=Movie_poster
        ,Languages=Languages, Gener= Gener,About_movie=About_movie, Movie_trailor= Movie_trailor
        ,Movie_duaration=Movie_duration)
        obj.save()
        return redirect("add-movie")

    return render(request,"add-movie.html")    

def AdminDashboard(request):
    movie=Movies.objects.all()
    return render(request,"admin-dashboard.html",{"data":movie})


def ViewUser(request):
    userdata=User.objects.all()
    return render(request,"view-user.html",{"data":userdata})   



def ViewBooking(request):
    Bookingdata=Booking.objects.all()
    return render(request,"admin-view-booking.html",{"data":Bookingdata})     

