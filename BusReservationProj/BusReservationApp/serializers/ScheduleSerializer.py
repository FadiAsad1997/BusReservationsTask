from marshmallow_sqlalchemy import ModelSchema
from BusReservationApp.models.Schedule import Schedule
from BusReservationApp.components import session
import time


class ScheduleSerializer(ModelSchema):

    class Meta:
        model = Schedule
        fields = ("busID", "srcStationID", "dstStationID", "srcTimeStamp", "dstTimeStamp", "isAvailable")


