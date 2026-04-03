from flask import Flask
from .config import Config
from .extensions import db, migrate

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    migrate.init_app(app, db)

     # Import models here so Alembic can detect them
    # IMPORT MODELS HERE so Alembic knows them
    from .models.user import User
    from .models.booking import Booking
    from .models.group import Group
    from .models.timeslot import TimeSlot

    # Register routes
    from .routes.booking_routes import booking_bp
    from .routes.timeslot_routes import timeslot_bp

    app.register_blueprint(booking_bp, url_prefix="/bookings")
    app.register_blueprint(timeslot_bp, url_prefix="/timeslots")

    return app