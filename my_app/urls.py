from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token


router = DefaultRouter()

router.register('flights',views.FlightViewSet)
router.register('passenger',views.PassengerViewSet)
router.register('reservation',views.ReservationViewSet)


urlpatterns = [
    path('flight-services/',include(router.urls)),
    path('flight-services/find-flight/',views.find_flight),
    path('flight-services/save_reservation/',views.save_reservation),
    path('api-token-auth/',obtain_auth_token,name='api_auth_token')
]