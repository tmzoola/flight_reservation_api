from django.contrib import admin
from .models import Reservation,Flight,Passenger


admin.site.register([Reservation,Flight,Passenger])

