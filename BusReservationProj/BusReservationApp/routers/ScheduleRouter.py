from rest_framework_nested import routers
from BusReservationApp.views.ScheduleView import ScheduleView

scheduleRouter = routers.SimpleRouter()
scheduleRouter.register(r'schedules', ScheduleView, basename='schedule')
