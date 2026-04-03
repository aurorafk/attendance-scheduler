from app.extensions import db

class TimeSlot(db.Model):
    __tablename__ = "time_slot"
    id = db.Column(db.Integer, primary_key=True)
    group_id = db.Column(db.Integer, db.ForeignKey('group.id'))
    date = db.Column(db.Date)
    start_time = db.Column(db.Time)
    end_time = db.Column(db.Time)
    capacity = db.Column(db.Integer)
    booked_count = db.Column(db.Integer, default=0)