from BusReservationApp.serializers.ScheduleSerializer import ScheduleSerializer
from BusReservationApp.components.SchedulesComponent import ScheduleComponent
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from jsonschema import validate, exceptions as jsonschema_exceptions
import json

class ScheduleView(viewsets.ViewSet):
    def list(self, request):
        schedules = ScheduleComponent.getAvailableSchedules()
        serializer = ScheduleSerializer().dump(schedules, many=True)
        return Response(serializer, status=status.HTTP_200_OK)

    def create(self, request):

        schedule = ScheduleComponent.setSchedule(busID=self.request.data['busID'], srcStationID=self.request.data['srcStationID'],
                                                   dstStationID=self.request.data['dstStationID'], srcTimeStamp=self.request.data['srcTimeStamp'],
                                                   dstTimeStamp=self.request.data['dstTimeStamp'], isAvailable=self.request.data['isAvailable'])
        serializer = ScheduleSerializer().dump(schedule)
        if serializer:
            return Response(serializer, status=status.HTTP_201_CREATED)
        return Response(serializer, status=status.HTTP_400_BAD_REQUEST)
