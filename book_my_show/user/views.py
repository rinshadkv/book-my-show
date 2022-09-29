from email import message
import json
from multiprocessing import context
from sre_constants import SUCCESS
from urllib import request
from django.shortcuts import render,redirect,HttpResponse

from localadmin.models import Movies
from .models import *
from django.http.response import JsonResponse
# Create your views here.

def Home(request):
    movie_data=Movies.objects.all()
    context={
        "data":movie_data
    }
    print(movie_data)

    return render(request,"index.html",context)


def Login(request):
  

   
    email=request.POST['email']
    password=request.POST['password']
    
    try:
        data=User.objects.get(email=email,password=password)
        request.session['user_id']=data.id
        
        return redirect("home")
    except:

        errormessage="email or password not correct"
        print(errormessage)

           

    return redirect("home")    
def CheckEmail(request):
    email=request.GET['email']
    data=User.objects.filter(email=email).exists()
    return JsonResponse({"exists":data})
            

def LogOut(request):
    del request.session['user_id']
    request.session.flush()

    return redirect('home')            
   
       

def UserSignup(request):
    
 
        email=request.POST['signup_email']
        password=request.POST['signup_password']
        name=request.POST['username']
        obj=User(email=email,password=password,name=name)   
        obj.save()  
        request.session['user_id']=obj.id
        return redirect("home")
    
def MovieDetails(request,id):
    movie=Movies.objects.get(id=id)


    return render(request,"movie-details.html",{"data":movie})

def BuyTicketsPage(request,id):
    movie=Movies.objects.get(id=id)
   
    return render(request,"book-ticket.html",{"data":movie})    


def BookTicket(request):

    selected_seat=[]
    if request.method=="POST":

        customer_id=User.objects.get(id=request.session["user_id"])
        movie_id=Movies.objects.get(id=request.POST["movie_id"])
        movie_name=request.POST['movie_name']
        show_date=request.POST['show_date']
        show_time=request.POST["show_time"]
        seat_category=request.POST["seat_category"]
        totel_seats=request.POST["number-of-seats"]
        selected_seats=request.POST.getlist("selected_seat")
        premium_ticket=250
        standerd_ticket=150
        if seat_category  =="premium":
            totel_amount=  premium_ticket *int(totel_seats) 
        else :
           totel_amount=int(totel_seats)*standerd_ticket
   
        payment_status="done"
        print(
            totel_amount,totel_seats,seat_category,show_date,show_time,selected_seats

        )
        obj=Booking(Customer=customer_id,Movie_name=movie_name,Booking_date=show_date,
        Booking_time=show_time,Seat_category=seat_category,Totel_seats=totel_seats,Movie_id=movie_id,
        Selected_seats=selected_seats,Totel_amount=totel_amount,Payment_status=payment_status)
        obj.save()
        print(totel_amount)
        return redirect("home")
    else:
        pass
    return redirect("movie")    

def ViewBooking(request):
    booking_data=Booking.objects.filter(Customer_id=request.session["user_id"])
    context={
        "data":booking_data
    }
    return render(request,"view-booking.html",context)

def AvilableSeats(request):
    movie_id=Movies.objects.get(id=request.GET["movie_id"])

    show_date=request.GET['show_date']
    show_time=request.GET["show_time"]
    seat_category=request.GET["seat_category"]
    totel_seats=request.GET["number-of-seats"]

    avilable_seats=Booking.objects.filter(movie_id_id=movie_id,Booking_date=show_date,
        Booking_time=show_time,Seat_category=seat_category,Totel_seats=totel_seats,Movie_id=movie_id,
        ).exists()
    

    return JsonResponse({"yes":avilable_seats})         


        
       
