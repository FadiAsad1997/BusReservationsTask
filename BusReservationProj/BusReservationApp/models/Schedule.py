from BusReservationApp.models import Base
from sqlalchemy import Column, Integer, ForeignKey, Boolean, BigInteger,String
from sqlalchemy.orm import relationship


class Driver(Base):
    __tablename__ = "driver"

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_Name = Column(String)
    last_Name = Column(String)
    bus = relationship("Bus", uselist=False, back_populates="driver")


class Bus(Base):
    __tablename__ = 'bus'

    id = Column(Integer, primary_key=True, autoincrement=True)
    driver_id = Column(Integer, ForeignKey('driver.id'))
    driver = relationship("Driver", uselist=False, back_populates="bus")


class Station(Base):
    __tablename__ = "station"

    id = Column(Integer, primary_key=True, autoincrement=True)
    city = Column(String)
    street = Column(String)


class Schedule(Base):
    __tablename__ = "schedule"

    id = Column(Integer, primary_key=True, autoincrement=True)
    busID = Column(Integer, ForeignKey('bus.id'))
    srcStationID = Column(Integer, ForeignKey('station.id'))
    dstStationID = Column(Integer, ForeignKey('station.id'))
    srcTimeStamp = Column(BigInteger)
    dstTimeStamp = Column(BigInteger)
    isAvailable = Column(Boolean)

