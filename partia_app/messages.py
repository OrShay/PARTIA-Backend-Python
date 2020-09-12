from flask_request_validator import (
    Param,
    GET,
    validate_params
)
from marshmallow import ValidationError
from flask import Blueprint, request
from partia_app import validator, responses
from app_engine import AppEngine

messages_blueprint = Blueprint('messages_blueprint', __name__)


@messages_blueprint.route('/messages', methods=['POST'])
def add_message():
    try:
        request_dict = validator.MessageSchema().load(request.json)
        pin_code = request_dict["pin_code"]
        event = AppEngine.get_event_by_pin_code(pin_code)
        if not event:
            return responses.response_invalid_event()
        event.add_message(request_dict["title"], request_dict["text"], request_dict["author"])
        return responses.response_200(request_dict)
    except ValidationError as errors:
        return responses.response_invalid_request(errors.messages)


@messages_blueprint.route('/messages', methods=['GET'])
@validate_params(Param('pin_code', GET, int, required=True))
def get_messages_board(pin_code):
    event = AppEngine.get_event_by_pin_code(pin_code)
    if not event:
        return responses.response_invalid_event()
    messages_list = event.get_messages()
    return responses.response_200({"messages": messages_list})
