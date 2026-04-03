from app.extensions import db

class Booking(db.Model):
    __tablename__ = "booking"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    timeslot_id = db.Column(db.Integer, db.ForeignKey('time_slot.id'))