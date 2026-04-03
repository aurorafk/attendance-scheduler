from app.models.timeslot import TimeSlot
from sqlalchemy.orm.exc import NoResultFound

class TimeSlotRepository:
    def __init__(self, db_session):
        self.db = db_session  # ✅ consistent naming

    def get_for_update(self, timeslot_id):
        try:
            timeslot = (
                self.db.query(TimeSlot)
                .filter_by(id=timeslot_id)
                .with_for_update()   # ✅ row-level lock (IMPORTANT)
                .one()
            )
            return timeslot  # ✅ return result
        except NoResultFound:
            raise ValueError("Timeslot not found")

    def save(self, slot):
        self.db.add(slot)