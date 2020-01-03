from BusReservationApp.models import Base
from sqlalchemy import Column, Integer, ForeignKey, Table

reservation_schedule = Table('reservation_schedule', Base.metadata,
                             Column('id', Integer, primary_key=True, autoincrement=True),
                             Column('ScheduleID', Integer, ForeignKey('schedule.id')),
                             Column('ReservationID', Integer, ForeignKey('reservation.id'))
)
