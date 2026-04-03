from flask import Blueprint, request, jsonify
from app.di.container import Container

timeslot_bp = Blueprint("timeslot", __name__)

@timeslot_bp.route("/timeslots", methods=["POST"])
def create_timeslot():
    data = request.get_json()

    service = Container.timeslot_service()

    timeslot = service.create_timeslot(
        start_time=data["start_time"],
        end_time=data["end_time"],
        group_id=data["group_id"]
    )

    return jsonify({
        "id": timeslot.id
    }), 201