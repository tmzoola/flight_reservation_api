from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('flights',views.FlightViewSet)
router.register('passenger',views.PassengerViewSet)
router.register('reservation',views.ReservationViewSet)


urlpatterns = [
    path('flight-services/',include(router.urls)),
    path('flight-services/find-flight/',views.find_flight)
]