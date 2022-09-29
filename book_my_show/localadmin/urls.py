
from importlib.resources import path
from unicodedata import name
from django.urls import path
from localadmin import views 
urlpatterns = [
    path("admin",views.AdminLogin,name="admin-login"),
    path("add-movie",views.AddMovie,name="add-movie"),
    path("admin-dashboard",views.AdminDashboard,name="admin-dashboard",),
    path("view-user",views.ViewUser,name="view-user"),
    path("admin-view-booking",views.ViewBooking,name="view-bookings")

    
]
