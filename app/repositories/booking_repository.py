from app.models.booking import Booking

class BookingRepository:
    def __init__(self, db_session):
        self.db = db_session

    def create(self, user_id, timeslot_id):
        booking = Booking(user_id=user_id, timeslot_id=timeslot_id)
        self.db.add(booking)
        return booking