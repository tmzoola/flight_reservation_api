from django.db import models

# Create your models here.
class Flight(models.Model):
    flightNumber = models.CharField(max_length=20)
    operatingAirlines = models.CharField(max_length=20)
    departureCity = models.CharField(max_length=20)
    arrivalCity = models.CharField(max_length=20)
    dateOfDeparture = models.DateField()
    estimatedTimeofDeparture = models.TimeField()

    def __str__(self):
        return f"{self.operatingAirlines}  {self.flightNumber}"
    


class Passenger(models.Model):
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    middleName = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.firstName} {self.lastName}"
    


class Reservation(models.Model):
    flight = models.OneToOneField(Flight,on_delete=models.CASCADE)
    passenger = models.OneToOneField(Passenger,on_delete=models.CASCADE)
