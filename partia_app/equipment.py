from flask_request_validator import Param, GET, validate_params
from flask import Blueprint, request
from partia_app import validator, responses
from app_engine import AppEngine
from item import ItemEncoder
import json
equipment_blueprint = Blueprint('equipment_blueprint', __name__)


@equipment_blueprint.route('/equipment', methods=['GET'])
@validate_params(Param('pin_code', GET, int, required=True))
def get_equipment_list(pin_code):
    event = AppEngine.get_event_by_pin_code(pin_code)
    if not event:
        return responses.response_invalid_event()
    items_dict = event.get_equipment_list()
    json_response = {}
    try:
        for key, val in items_dict.items():
            json_response[key] = json.loads(ItemEncoder().encode(val))
    except Exception as e:
        return responses.response_internal_error(e)
    return responses.response_200(json_response)

