# from BusReservationProj.BusReservationApp.models import Base
# from sqlalchemy import Column, Integer, String
# from sqlalchemy.orm import relationship
# from BusReservationProj.BusReservationApp.models.Schedule import Bus
#
# class Driver(Base):
#     __tablename__ = "driver"
#
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     first_Name = Column(String)
#     last_Name = Column(String)
#     bus = relationship("Bus", uselist=False, back_populates="driver")
