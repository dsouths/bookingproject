from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import BookingForm
import datetime
from django.contrib import messages


# Create your views here.

def index(request):
    """This view renders the index.html page
    and extends the base.html page
    """
    return render(request, 'index.html')


def services(request):
    """
    This view renders to the user the services page.
    """
    services = Service.objects.all()
    return render(request, 'services.html', {'services': services})

def booknow(request):
    """The view for the booking page. If user is logged in it renders the
    booknow.html, otherwise it redirects user to the login page or signup page.
    """
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking_form = form.save(commit=False)
            booking_form.user = request.user
            booking_form.save()
            return redirect('bookings')
        else:
            messages.error(request, "Please enter correct data")
            return render(request, 'booknow.html', {'form': form})
    form = BookingForm()
    return render(request, 'booknow.html', {'form': form})


def bookings(request):
    """This view checks if user is logged in and renders the
    bookings.html page which shows user bookings and otherwise
    it redirects to the signup page
    """
    if request.user.is_authenticated:
        bookings = Booking.objects.filter(user=request.user)
        context = {
           'bookings': bookings
        }
        return render(request, 'bookings.html', context)
    else:
        return redirect('../accounts/signup')


def change_booking(request, booking_id):
    """The view that renders the change_booking page where the user can
    update a current booking.
    """
    record = get_object_or_404(Booking, id=booking_id)

    if request.method == 'POST':
        form = BookingForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            messages.success(request, 'You succesfully updated your booking.')
            return redirect('bookings')
        else:
            return render(request, 'change-booking.html', {'form': form})
    form = BookingForm(instance=record)
    context = {'form': form, 'record': record}
    return render(request, 'change-booking.html', context)


def delete_booking(request, booking_id):
    """
    Function enables user to delete a booking record
    """

    record = get_object_or_404(Booking, id=booking_id)
    if request.method == "POST":
        form = BookingForm(request.POST, instance=record)
        if record.delete():
            messages.success(request, 'Your booking has been deleted.')
            return redirect('bookings')

    form = BookingForm(instance=record)
    context = {
        'form': form, 'record': record}
    return render(request, 'delete-booking.html', context)