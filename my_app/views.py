from django.shortcuts import render
from .models import Reservation,Flight,Passenger
from .serializers import FlightSerializer,PassengerSerializer,ReservationSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


@api_view(['POST'])
def find_flight(request):
    flights = Flight.objects.filter(departureCity=request.data['departureCity'],
                                    arrivalCity=request.data['arrivalCity'],
                                    dateOfDeparture=request.data['dateOfDeparture'])
    serializer = FlightSerializer(flights,many=True)

    return Response(serializer.data)

@api_view(['POST'])
def save_reservation(request):
    flight = Flight.objects.get(id=request.data['flight_id'])

    passenger = Passenger()
    passenger.firstName=request.data['firstName']
    passenger.lastName=request.data['lastName']
    passenger.middleName=request.data['middleName']
    passenger.email=request.data['email']
    passenger.phone_number=request.data['phone_number']
    passenger.save()

    reservation = Reservation()
    reservation.flight = flight
    reservation.passenger =  passenger
    reservation.save()

    return Response(status=status.HTTP_201_CREATED)

class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    permission_classes=(IsAuthenticated,)

class PassengerViewSet(viewsets.ModelViewSet):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer

class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer


