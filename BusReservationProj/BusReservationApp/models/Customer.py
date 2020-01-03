from BusReservationProj.BusReservationApp.models import Base
from sqlalchemy import Column, Integer, String


class Customer(Base):
    __tablename__ = "customer"

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_Name = Column(String)
    last_Name = Column(String)
