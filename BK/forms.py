from django import forms
from .models import Booking, Dentist
from django.core.validators import MinValueValidator
import datetime

# A function that does not allow you to select dates
#  earlier than today's date. Source: github manual
# code https://gist.github.com/stasyao/99376eb0cf0ad3599f9737c421b5210e#part_4


def get_min_date():
    """Returns the current date plus 2 days, so the user
    can book appointment 2 days in advance
     """
    return datetime.date.today() + datetime.timedelta(days=2)


class DateInput(forms.DateInput):
    """This class provides a calendar widget that the user can
    pick the booking date.
    """
    input_type = 'date'


class BookingForm(forms.ModelForm):
    """This class generates a form from the Booking model
    """

    date = forms.DateField(
        validators=[MinValueValidator(get_min_date)],
        widget=DateInput(attrs={'type': 'date', 'min': get_min_date}))

    class Meta:
        model = Booking
        fields = ('name', 'phone', 'email', 'service', 'date', 'time')
        widgets = {'date': DateInput()}
    
    dentist = forms.ModelChoiceField(queryset=Dentist.objects.all())
    
    def clean_date(self):
        date = self.cleaned_data['date']
        if date.weekday() >= 5:  # Saturday or Sunday
            raise forms.ValidationError("Bookings are only available from Monday to Friday.")
        return date