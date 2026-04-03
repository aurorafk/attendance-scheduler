from app.extensions import db
from app.repositories.timeslot_repository import TimeSlotRepository
from app.repositories.booking_repository import BookingRepository
from app.services.booking_service import BookingService
from app.services.timeslot_service import TimeSlotService

class Container:

    @staticmethod
    def booking_service():
        db_session = db.session

        timeslot_repo = TimeSlotRepository(db_session)
        booking_repo = BookingRepository(db_session)

        return BookingService(db_session, timeslot_repo, booking_repo)
    
    @staticmethod
    def timeslot_service():
        repo = TimeSlotRepository(db.session)
        return TimeSlotService(db.session, repo)