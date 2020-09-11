from flask import Blueprint, request
from partia_app import validator
from partia_app import responses
from app_engine import AppEngine

login_blueprint = Blueprint('login_blueprint', __name__)


def check_credentials_exist(user_request):
    errors = validator.Login().validate(user_request.json)
    if errors:
        return None, errors
    user_email = user_request.json["userEmail"]
    password = user_request.json['password']
    return user_email, password


@login_blueprint.route('/login', methods=['POST'])
def login_to_app():
    username, password = check_credentials_exist(request)
    if not username:
        return responses.response_invalid_request(password)
    if AppEngine.is_logged_user(username, password):
        return responses.response_200({"message": "Valid credentials"})
    return responses.response_wrong_credentials()


@login_blueprint.route('/signup', methods=['POST'])
def sign_up():
    username, password = check_credentials_exist(request)
    if not username:
        return responses.response_invalid_request(password)
    if AppEngine.signup_new_user(username, password):
        return responses.response_200({"message": "user was added successfully"})
    else:
        return responses.response_invalid_user_name()
