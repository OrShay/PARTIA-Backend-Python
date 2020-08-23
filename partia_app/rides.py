from flask import Blueprint, request
from partia_app import validator, responses
from app_engine import AppEngine

rides_blueprint = Blueprint('rides_blueprint', __name__)


@rides_blueprint.route('/rides', methods=['POST'])
def add_ride():
    errors = validator.RideScheme().validate(request.json)
    if errors:
        return responses.response_invalid_request(errors)
    event = AppEngine.get_event_by_pin_code(request.json["pin_code"])
    if not event:
        return responses.response_invalid_event()
    try:
        driver_user_name = request.json['driver_user_name']
        driver = event.participants_dict[driver_user_name]
        source = request.json['source']
        available_seats = request.json['available_seats']
        departure_time = request.json['departure_time']
        event.rides_board.add_ride(driver, available_seats, source, departure_time)
        return responses.response_200({"response": "added ride"})
    except KeyError:
        return responses.response_invalid_user_name()
