from rest_framework_nested import routers
from BusReservationApp.views.ReservationView import ReservationView

reservationRouter = routers.SimpleRouter()
reservationRouter.register('reservation', ReservationView, basename='reservation')


