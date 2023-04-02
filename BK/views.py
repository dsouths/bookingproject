from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import BookingForm
import datetime
from django.contrib import messages


# Create your views here.
