import constants
from marshmallow import Schema, fields, validate


class EventScheme(Schema):
    name = fields.Str(required=True)
    location = fields.Str(required=True)
    info = fields.Str(required=True)
    environment = fields.Str(validate=validate.OneOf(constants.Environment.__members__.keys()), required=True)
    kind_of_event = fields.Str(validate=validate.OneOf(constants.KindOfEvent.__members__.keys()), required=True)
    date = fields.DateTime(required=True)
    meal_organization = fields.Str(validate=validate.OneOf(constants.Organization.__members__.keys()),
                                   allow_none=True,
                                   required=True)
    beverage_organization = fields.Str(validate=validate.OneOf(constants.Organization.__members__.keys()),
                                       allow_none=True,
                                       required=True)


class QuerySchema(Schema):
    VEGETARIAN = fields.Bool(required=True)
    VEGAN = fields.Bool(required=True)
    KOSHER = fields.Bool(required=True)
    GLUTEN_FREE = fields.Bool(required=True)
    LACTOSE_FREE = fields.Bool(required=True)
    FISH = fields.Bool(required=True)
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
    event_pin_code = fields.Int(required=True)
    user_name = fields.Str(required=True)
    query_answers = fields.Nested(QuerySchema, required=True)


class KindOfMEalScheme(Schema):
    pin_code = fields.Int(required=True)
    kind_of_meal = fields.Str(validate=validate.OneOf(constants.KindOfMeal.__members__.keys()),
                              allow_none=True,
                              required=True)


class RideScheme(Schema):
    pin_code = fields.Int(required=True)
    driver_user_name = fields.Str(required=True)
    source = fields.Str(required=True)
    available_seats = fields.Int(required=True)
    departure_time = fields.DateTime(required=True, allow_none=True)