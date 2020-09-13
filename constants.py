from enum import Enum


class Organization(Enum):
    MULTIPLE_INCHARGES = 1
    SINGLE_INCHARGE = 2
    OUTSOURCE_INCHARGE = 3


class KindOfEvent(Enum):
    BACHELORETTE = 1
    BIRTHDAY = 2
    GATHERING = 3


class Environment(Enum):
    OUTDOORS = 1
    INDOORS = 2


class FoodPreference(Enum):
    VEGETARIAN = 1
    VEGAN = 2
    KOSHER = 3
    GLUTEN_FREE = 4
    LACTOSE_FREE = 5


class Beverages(Enum):
    BEER = 1
    RED_WINE = 2
    WHITE_WINE = 3
    VODKA_GLASS = 4
    VODKA_SHOT = 5
    WHISKEY_GLASS = 6
    WHISKEY_SHOT = 7
    TEQUILA_GLASS = 8
    TEQUILA_SHOT = 9
    CAMPARI_GLASS = 10
    CAMPARI_SHOT = 11
    ARAK_GLASS = 12
    ARAK_SHOT = 13
    GIN_GLASS = 14
    GIN_SHOT = 15


class KindOfMeal(Enum):
    MEAT = 1
    DAIRY = 2


class EventState(Enum):
    GENERATING = 1
    IN_PROGRESS = 2
    FINISHED = 3


EQUIPMENT_LIST_FILE_TEMPLATE = "files/{}_equipment_list.json"
