from flask_request_validator import (
    Param,
    GET,
    validate_params
)
from marshmallow import ValidationError
from flask import Blueprint, request
from partia_app import validator, responses
from app_engine import AppEngine

event_blueprint = Blueprint('event_blueprint', __name__)


@event_blueprint.route('/event', methods=['POST'])
def create_new_event():
    errors = validator.EventScheme().validate(request.json)
    if errors:
        return responses.response_invalid_request(errors)
    pin_code = AppEngine.create_new_event(request.json)
    event = AppEngine.get_event_by_pin_code(pin_code)
    return responses.response_200(event.get_event_info())


@event_blueprint.route('/event', methods=['GET'])
@validate_params(Param('pin_code', GET, int, required=True))
def get_event_info(pin_code):
    event = AppEngine.get_event_by_pin_code(pin_code)
    if not event:
        return responses.response_invalid_event()
    return responses.response_200(event.get_event_info())


@event_blueprint.route('/event/food_statistics', methods=['GET'])
@validate_params(Param('pin_code', GET, int, required=True))
def get_food_statistics(pin_code):
    event = AppEngine.get_event_by_pin_code(pin_code)
    if not event:
        return responses.response_invalid_event()
    return responses.response_200(event.get_food_statistics())


@event_blueprint.route('/event/beverage_statistics', methods=['GET'])
@validate_params(Param('pin_code', GET, int, required=True))
def get_beverage_statistics(pin_code):
    event = AppEngine.get_event_by_pin_code(pin_code)
    if not event:
        return responses.response_invalid_event()
    return responses.response_200(event.get_beverages_statistics())


@event_blueprint.route('/event/set-date', methods=['PUT'])
def set_date():
    try:
        request_dict = validator.EventDate().load(request.json)
        pin_code = request_dict["pin_code"]
        event = AppEngine.get_event_by_pin_code(pin_code)
        if not event:
            return responses.response_invalid_event()
        event.set_date(request_dict["date"])
        return responses.response_200(request_dict)
    except ValidationError as errors:
        return responses.response_invalid_request(errors.messages)


@event_blueprint.route('/event/kind_of_meal', methods=['POST'])
def set_kind_of_meal():
    try:
        request_dict = validator.KindOfMEalScheme().load(request.json)
        pin_code = request_dict["pin_code"]
        event = AppEngine.get_event_by_pin_code(pin_code)
        if not event:
            return responses.response_invalid_event()
        event.set_kind_of_meal(request_dict["kind_of_meal"])
        return responses.response_200(request_dict)
    except ValidationError as errors:
        return responses.response_invalid_request(errors.messages)


@event_blueprint.route('/event/set-info', methods=['PUT'])
def set_info():
    try:
        request_dict = validator.EventInfo().load(request.json)
        pin_code = request_dict["pin_code"]
        event = AppEngine.get_event_by_pin_code(pin_code)
        if not event:
            return responses.response_invalid_event()
        event.set_info(request_dict["info"])
        return responses.response_200(event.get_event_info())
    except ValidationError as errors:
        return responses.response_invalid_request(errors.messages)


@event_blueprint.route('/event/participants', methods=['GET'])
@validate_params(Param('pin_code', GET, int, required=True))
def get_all_participants(pin_code):
    event = AppEngine.get_event_by_pin_code(pin_code)
    if not event:
        return responses.response_invalid_event()
    participants_list = list(event.participants_dict.keys())
    return responses.response_200({"participants": participants_list})
