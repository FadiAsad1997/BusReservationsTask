from BusReservationApp.models import Base
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from BusReservationApp.models.ReservationSchedule import reservation_schedule
from BusReservationApp.models.Schedule import Schedule

class Reservation(Base):
    __tablename__ = 'reservation'

    id = Column(Integer, primary_key=True, autoincrement=True)
    customerid = Column(Integer, ForeignKey('customer.id'))
    schedules = relationship("Schedule", secondary=reservation_schedule)
