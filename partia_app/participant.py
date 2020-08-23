from flask import Blueprint, request
from partia_app import validator, responses
from app_engine import AppEngine

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
        return responses.response_200({"pin_code": event_pin_code})
    else:
        return responses.response_invalid_user_name()

