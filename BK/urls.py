from django.urls import path
from . import views

urlpatterns = [
     path('', views.index, name="index"),
     path('services/', views.services, name="services"),
     path('booknow/', views.booknow, name="booknow"),
     path('bookings/', views.bookings, name='bookings'),
     path('change/<int:booking_id>/', views.change_booking, name='change_booking'),
     path('delete-booking/<int:booking_id>/', views.delete_booking, name='delete_booking'),
    
]