from flask import Blueprint, request, jsonify
from app.di.container import Container

booking_bp = Blueprint("booking", __name__)

@booking_bp.route("/", methods=["POST"])
def create_booking():
    data = request.get_json()

    service = Container.booking_service()

    result = service.book_slot(
        user_id=data["user_id"],
        timeslot_id=data["timeslot_id"]
    )

    return jsonify(result)