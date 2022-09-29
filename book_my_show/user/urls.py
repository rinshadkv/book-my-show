from django.urls import path
from . import views

urlpatterns = [
    path("",views.Home,name="home"),
    path ('signup/',views.UserSignup,name="signup"),
    path('login',views.Login,name="login"),
    path("logout",views.LogOut,name="logout"),
    path("book-ticket",views.BookTicket,name="book-ticket"),
    path("movie/<int:id>",views.MovieDetails,name="movie"),
    path("buy-tickets/<int:id>",views.BuyTicketsPage,name="buy-tickets"),
    path("view-booking",views.ViewBooking,name="view-booking"),
    path("check_avilable/",views.AvilableSeats),
    path("check_email/",views.CheckEmail),


]
