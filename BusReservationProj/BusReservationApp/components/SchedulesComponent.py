from . import session
from BusReservationApp.models.Schedule import Schedule

class ScheduleComponent:
    @staticmethod
    def getAvailableSchedules():
        schedules = session.query(Schedule).all()
        return schedules

    @staticmethod
    def setSchedule(**kwargs):
        schedule = Schedule(**kwargs)
        session.add(schedule)
        session.commit()
        return schedule
