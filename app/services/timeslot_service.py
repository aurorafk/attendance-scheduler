from app.models.timeslot import TimeSlot

class TimeSlotService:
    def __init__(self, db_session, timeslot_repo):
        self.db = db_session
        self.repo = timeslot_repo

    def create_timeslot(self, start_time, end_time, group_id):
        slot = TimeSlot(
            start_time=start_time,
            end_time=end_time,
            group_id=group_id
        )

        self.repo.save(slot)
        self.db.commit()

        return slot