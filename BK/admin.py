from django.contrib import admin
from .models import Service
from BK.models import Booking

# Register your models here.

@admin.register(Dentist)

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("service_name", "price")


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    """
    Class registered to represent model in admin database.
    """
    list_display = ('user', 'name',
                    'date',
                    'time',
                    'phone',
                    'email',
                    'service'
                    )
    search_fields = ('user',
                     'name',
                     'date',
                     'phone')
    list_filter = ('user',
                   'name',
                   'date',
                   'phone')