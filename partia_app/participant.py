from flask import Blueprint, request
from partia_app import validator, responses
from app_engine import AppEngine
from flask_request_validator import (
    Param,
    GET,
    validate_params
)

participant_blueprint = Blueprint('participant_blueprint', __name__)


@participant_blueprint.route('/participant', methods=['POST'])
def add_new_participant():
    errors = validator.ParticipantScheme().validate(request.json)
    if errors:
        return responses.response_invalid_request(errors)
    event_pin_code = request.json["event_pin_code"]
    event = AppEngine.get_event_by_pin_code(event_pin_code)
    if not event:
        return responses.response_invalid_event()
    if event.add_participant(request.json["user_name"], request.json["query_answers"]):
        return responses.response_200((event.get_event_info()))
    else:
        return responses.response_invalid_user_name()


@participant_blueprint.route('/participant/check-unique', methods=['GET'])
@validate_params(Param('pin_code', GET, int, required=True),
                 Param('user_name', GET, str, required=True))
def check_participant_user_name(pin_code, user_name):
    event = AppEngine.get_event_by_pin_code(pin_code)
    if not event:
        return responses.response_invalid_event()
    if user_name in event.participants_dict.keys():
        return responses.response_invalid_user_name()
    else:
        return responses.response_200({"message": "unique username"})


@participant_blueprint.route('/participant/is-owner', methods=['GET'])
@validate_params(Param('pin_code', GET, int, required=True),
                 Param('user_name', GET, str, required=True))
def is_participant_event_owner(pin_code, user_name):
    event = AppEngine.get_event_by_pin_code(pin_code)
    if not event:
        return responses.response_invalid_event()
    if user_name not in event.participants_dict.keys():
        return responses.response_invalid_user_name()
    is_owner = event.is_event_owner(user_name)
    return responses.response_200({"is_owner": is_owner})


@participant_blueprint.route('/participant/events', methods=['POST'])
def get_participant_events():
    user_email = request.json.get('userEmail', None)
    if not user_email:
        return responses.response_invalid_request({"message": "UserEmil is required"})
    if user_email not in AppEngine.users_dict.keys():
        return responses.response_invalid_user_name()
    events_dict = AppEngine.get_user_events(user_email)
    return responses.response_200(events_dict)
