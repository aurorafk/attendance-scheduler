from app.extensions import db
class BookingService:
    def __init__(self, db_session, timeslot_repo, booking_repo):
        self.db = db_session
        self.timeslot_repo = timeslot_repo
        self.booking_repo = booking_repo

    def book_slot(self, user_id, timeslot_id):
        try:
            with self.db.begin():

                slot = self.timeslot_repo.get_for_update(timeslot_id)

                if slot.booked_count >= slot.capacity:
                    raise Exception("Slot is full")

                self.booking_repo.create(user_id, timeslot_id)

                slot.booked_count += 1

            return {"message": "Booking successful"}

        except Exception as e:
            return {"error": str(e)}
    
    