from flask_request_validator import (
    Param,
    GET,
    validate_params
)
from marshmallow import ValidationError
from flask import Blueprint, request
from partia_app import validator, responses
from app_engine import AppEngine

cashier_blueprint = Blueprint('cashier_blueprint', __name__)


@cashier_blueprint.route('/cashier', methods=['GET'])
@validate_params(Param('pin_code', GET, int, required=True))
def get_current_money_spent(pin_code):
    event = AppEngine.get_event_by_pin_code(pin_code)
    if not event:
        return responses.response_invalid_event()
    money_spent = event.cashier.get_money_spent()
    return responses.response_200({"money_spent": money_spent})


@cashier_blueprint.route('/cashier/owes', methods=['GET'])
@validate_params(Param('pin_code', GET, int, required=True),
                 Param('userEmail', GET, str, required=True))
def get_participant_owes(pin_code, userEmail):
    event = AppEngine.get_event_by_pin_code(pin_code)
    if not event:
        return responses.response_invalid_event()
    try:
        owes = event.split_investment()[userEmail]
        return responses.response_200({"owes": owes})
    except KeyError:
        return responses.response_invalid_user_name()


@cashier_blueprint.route('/cashier/split', methods=['GET'])
@validate_params(Param('pin_code', GET, int, required=True))
def get_all_participants_owes(pin_code):
    event = AppEngine.get_event_by_pin_code(pin_code)
    if not event:
        return responses.response_invalid_event()
    owes_list = event.split_investment()
    return responses.response_200(owes_list)
