# from BusReservationProj.BusReservationApp.models import Base
# from sqlalchemy import Column, Integer, ForeignKey
# from sqlalchemy.orm import relationship
# from BusReservationProj.BusReservationApp.models.Driver import Driver
#
#
# class Bus(Base):
#     __tablename__ = 'bus'
#
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     driver_id = Column(Integer, ForeignKey('driver.id'))
#     driver = relationship("Driver", uselist=False, back_populates="bus")