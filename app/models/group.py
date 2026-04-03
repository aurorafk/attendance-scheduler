from app.extensions import db

class Group(db.Model):
    __tablename__ = "group"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    max_capacity_per_slot = db.Column(db.Integer)