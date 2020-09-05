from flask_request_validator import Param, GET, validate_params
from flask import Blueprint, request
from partia_app import validator, responses
from app_engine import AppEngine
from item import ItemEncoder
from event import Event
import json

equipment_blueprint = Blueprint('equipment_blueprint', __name__)


def get_equipment_list_response(items_dict):
    """
    The function creates a dictionary with all items data
    """
    json_response = {}
    for key, val in items_dict.items():
        json_response[key] = json.loads(ItemEncoder().encode(val))
    return json_response


@equipment_blueprint.route('/equipment', methods=['GET'])
@validate_params(Param('pin_code', GET, int, required=True))
def get_equipment_list(pin_code):
    event = AppEngine.get_event_by_pin_code(pin_code)
    if not event:
        return responses.response_invalid_event()
    items_dict = event.get_equipment_list()
    try:
        json_response = get_equipment_list_response(items_dict)
    except Exception as e:
        return responses.response_internal_error(e)
    return responses.response_200(json_response)


@equipment_blueprint.route('/equipment/Item/price', methods=['PUT'])
def set_item_price():
    errors = validator.SetItemPrice().validate(request.json)
    if errors:
        return responses.response_invalid_request(errors)
    event = AppEngine.get_event_by_pin_code(request.json["pin_code"])
    if not event:
        return responses.response_invalid_event()
    title = request.json['title']
    price = request.json['price']
    who_paid = request.json['user_name']
    try:
        event.set_item_price(title, price, who_paid)
        return responses.response_200(json.loads(ItemEncoder().encode(event.get_equipment_list()[title])))
    except ValueError as ex:
        return responses.response_invalid_request({"message": str(ex)})


@equipment_blueprint.route('/equipment/Item/in-charge', methods=['PUT'])
def add_item_in_charge():
    errors = validator.AddItemInCharge().validate(request.json)
    if errors:
        return responses.response_invalid_request(errors)
    event = AppEngine.get_event_by_pin_code(request.json["pin_code"])
    if not event:
        return responses.response_invalid_event()
    title = request.json['title']
    amount = request.json['amount']
    in_charge = request.json['user_name']
    try:
        event.equipment_list.add_in_charge(title, in_charge, amount)
        return responses.response_200(json.loads(ItemEncoder().encode(event.get_equipment_list()[title])))
    except Exception as ex:
        return responses.response_invalid_request({"message": str(ex)})


@equipment_blueprint.route('/equipment/Item', methods=['POST'])
def add_item():
    errors = validator.Item().validate(request.json)
    if errors:
        return responses.response_invalid_request(errors)
    event = AppEngine.get_event_by_pin_code(request.json["pin_code"])
    if not event:
        return responses.response_invalid_event()
    title = request.json['title']
    amount = request.json['amount']
    try:
        event.equipment_list.add_new_item(title, amount)
        return responses.response_200(json.loads(ItemEncoder().encode(event.get_equipment_list()[title])))
    except Exception as ex:
        return responses.response_invalid_request({"message": str(ex)})


@equipment_blueprint.route('/equipment/Item', methods=['DELETE'])
def remove_item():
    errors = validator.DeleteItem().validate(request.json)
    if errors:
        return responses.response_invalid_request(errors)
    event = AppEngine.get_event_by_pin_code(request.json["pin_code"])
    try:
        event.remove_item(request.json["title"])
        return responses.response_200({"message": "deleted"})
    except ValueError as ex:
        return responses.response_invalid_request({"message": str(ex)})


@equipment_blueprint.route('/equipment/Item/amount', methods=['PUT'])
def set_item_amount():
    errors = validator.Item().validate(request.json)
    if errors:
        return responses.response_invalid_request(errors)
    event = AppEngine.get_event_by_pin_code(request.json["pin_code"])
    if not event:
        return responses.response_invalid_event()
    title = request.json['title']
    amount = request.json['amount']
    try:
        event.get_equipment_list()
        event.equipment_list.set_item_amount(title, amount)
        return responses.response_200(json.loads(ItemEncoder().encode(event.get_equipment_list()[title])))
    except ValueError as ex:
        return responses.response_invalid_request({"message": str(ex)})
