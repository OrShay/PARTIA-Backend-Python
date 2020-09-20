from utils import constants
from marshmallow import Schema, fields, validate


class EventScheme(Schema):
    owner = fields.Str(required=True)
    name = fields.Str(required=True)
    location = fields.Str(required=True)
    info = fields.Str(required=True)
    environment = fields.Str(validate=validate.OneOf(constants.Environment.__members__.keys()), required=True)
    kind_of_event = fields.Str(validate=validate.OneOf(constants.KindOfEvent.__members__.keys()), required=True)
    date = fields.Str(required=True)
    meal_organization = fields.Str(validate=validate.OneOf(constants.Organization.__members__.keys()),
                                   allow_none=True,
                                   required=False)
    beverage_organization = fields.Str(validate=validate.OneOf(constants.Organization.__members__.keys()),
                                       allow_none=True,
                                       required=False)


class QuerySchema(Schema):
    VEGETARIAN = fields.Bool(required=True)
    VEGAN = fields.Bool(required=True)
    KOSHER = fields.Bool(required=True)
    GLUTEN_FREE = fields.Bool(required=True)
    LACTOSE_FREE = fields.Bool(required=True)
    BEER = fields.Bool(required=True)
    RED_WINE = fields.Bool(required=True)
    WHITE_WINE = fields.Bool(required=True)
    VODKA_GLASS = fields.Bool(required=True)
    VODKA_SHOT = fields.Bool(required=True)
    WHISKEY_GLASS = fields.Bool(required=True)
    WHISKEY_SHOT = fields.Bool(required=True)
    TEQUILA_GLASS = fields.Bool(required=True)
    TEQUILA_SHOT = fields.Bool(required=True)
    CAMPARI_GLASS = fields.Bool(required=True)
    CAMPARI_SHOT = fields.Bool(required=True)
    ARAK_GLASS = fields.Bool(required=True)
    ARAK_SHOT = fields.Bool(required=True)
    GIN_GLASS = fields.Bool(required=True)
    GIN_SHOT = fields.Bool(required=True)


class ParticipantScheme(Schema):
    pin_code = fields.Int(required=True)
    userEmail = fields.Str(required=True)
    mealPreference = fields.Str(required=True,
                                validate=validate.OneOf(constants.FoodPreference.__members__.keys()),
                                allow_none=True)
    allergies = fields.Str(required=True, validate=validate.OneOf(constants.Allergies.__members__.keys()),
                           allow_none=True)
    glassPreference = fields.Str(required=True, validate=validate.OneOf(constants.BeveragesGlass.__members__.keys()))
    chaserPreference = fields.Str(required=True, validate=validate.OneOf(constants.BeveragesChaser.__members__.keys()))


class KindOfMEalScheme(Schema):
    pin_code = fields.Int(required=True)
    kind_of_meal = fields.Str(validate=validate.OneOf(constants.KindOfMeal.__members__.keys()),
                              allow_none=True,
                              required=True)


class EventDate(Schema):
    pin_code = fields.Int(required=True)
    date = fields.DateTime(required=True)


class MessageSchema(Schema):
    pin_code = fields.Int(required=True)
    title = fields.Str(required=True)
    text = fields.Str(required=True)
    author = fields.Str(required=True)


class EventInfo(Schema):
    pin_code = fields.Int(required=True)
    info = fields.Str(required=True)


class RideScheme(Schema):
    pin_code = fields.Int(required=True)
    driver_user_name = fields.Str(required=True)
    source = fields.Str(required=True)
    available_seats = fields.Int(required=True)
    departure_time = fields.DateTime(required=True, allow_none=True)


class SetItemPrice(Schema):
    pin_code = fields.Int(required=True)
    title = fields.Str(required=True)
    price = fields.Float(required=True)
    user_name = fields.Str(required=True)


class AddItemInCharge(Schema):
    pin_code = fields.Int(required=True)
    title = fields.Str(required=True)
    amount = fields.Int(required=True)
    user_name = fields.Str(required=True)


class Item(Schema):
    pin_code = fields.Int(required=True)
    title = fields.Str(required=True)
    amount = fields.Int(required=True)


class DeleteItem(Schema):
    pin_code = fields.Int(required=True)
    title = fields.Str(required=True)


class Login(Schema):
    userEmail = fields.Str(required=True)
    password = fields.Str(required=True)
