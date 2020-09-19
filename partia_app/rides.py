import json

from flask import Blueprint, request

from rides.ride import RideEncoder
from partia_app import validator, responses
from app_engine import AppEngine
from flask_request_validator import (
    Param,
    GET,
    validate_params
)

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


@rides_blueprint.route('/rides', methods=['GET'])
@validate_params(Param('pin_code', GET, int, required=True))
def get_rides(pin_code):
    event = AppEngine.get_event_by_pin_code(pin_code)
    if not event:
        return responses.response_invalid_event()
    rides_dict = event.rides_board.get_rides()
    json_response = {}
    try:
        for key, val in rides_dict.items():
            json_response[key] = json.loads(RideEncoder().encode(val))
    except Exception as e:
        return responses.response_internal_error(e)
    return responses.response_200(json_response)

