from marshmallow_sqlalchemy import ModelSchema
from BusReservationApp.models.Reservation import Reservation
from BusReservationApp.components import session


class ReservationsSerializer(ModelSchema):
    class Meta:
        model = Reservation
        fields = ("customer_id", "schedules")
