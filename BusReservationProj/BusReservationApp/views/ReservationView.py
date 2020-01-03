from BusReservationApp.serializers.ReservationsSerializer import ReservationsSerializer
from BusReservationApp.components.ReservationComponent import ReservationComponent
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status


class ReservationView(viewsets.ViewSet):
    def list(self, request):
        reservations = ReservationComponent.getUserReservation(customerid=self.request.query_params['customer_id'])
        serializer = ReservationsSerializer().dump(reservations, many=True)
        for i in reservations:
            print(i.__dict__)
        return Response(serializer, status=status.HTTP_200_OK)
