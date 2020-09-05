from flask import jsonify


def _send_response(response_json: dict, status_code: int):
    return jsonify(response_json), status_code


def response_200(response_json: dict):
    return _send_response(response_json, 200)


def response_invalid_event():
    return _send_response({"error_message": "Invalid Event Pin Code"}, 405)


def response_invalid_user_name():
    return _send_response({"error_message": "Invalid User Name"}, 405)


def response_invalid_request(errors: dict):
    return _send_response({"invalid_fields": errors}, 405)


def response_internal_error(exception):
    return _send_response({"exception": str(exception)}, 500)
