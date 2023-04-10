from django.db import models
from enum import unique
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

# Create your models here.


class Service(models.Model):
    """The model is used to display data about the services
    provided by the dental practice
    """
    service_name = models.CharField(max_length=150, unique=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        unique_together = ('service_name', 'price', )
        ordering = ['-price']

    def __str__(self):
        return f"{self.service_name}, {self.price}"


HOURS = (
    ('10:00', '10:00'),
    ('10:30', '10:30'),
    ('11:00', '11:00'),
    ('11:30', '12:30'),
    ('12:00', '12:00'),
    ('12:30', '12:30'),
    ('13:00', '13:00'),
    ('13:30', '13:30'),
    ('14:00', '14:00'),
    ('14:30', '14:30'),
    ('15:00', '15:00'),
    ('15:30', '15:30'),
    ('16:00', '16:00'),
    ('16:30', '16:30'),
)

DAYS = (
    ('Mon', 'Mon'),
    ('Tues', 'Tues'),
    ('Wed', 'Wed'),
    ('Thurs', 'Thurs'),
    ('Fri', 'Fri'),

)

class Booking(models.Model):

    """Model that is used to store the data that the user enters in the
    booking form
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=50)
    email = models.EmailField(blank=True, null=True)
    phoneRegex = RegexValidator(regex=r'^\+?1?\d{8,15}$',
                                message="Please enter a valid phone number,"
                                "e.g. 123456789. Up to 15 digits allowed.",
                                code="invalid")
    phone = models.CharField(validators=[phoneRegex], max_length=16,
                             null=True, blank=True)
    date = models.DateField()
    time = models.CharField(max_length=30, choices=HOURS, default='10:00')

    class Meta:
        unique_together = ('user', 'date', 'time', 'service')

    def __str__(self):
        return self.name
