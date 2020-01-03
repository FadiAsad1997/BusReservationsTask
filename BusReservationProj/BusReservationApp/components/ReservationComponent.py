from . import session
from BusReservationApp.models.Reservation import Reservation

class ReservationComponent:
    @staticmethod
    def getUserReservation(**kwargs):
        reservation = session.query(Reservation).filter_by(customerid=kwargs['customerid'])
        return reservation.all()
