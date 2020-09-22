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


class Allergies(Enum):
    PEANUTS = 1
    GLUTEN_FREE = 4
    LACTOSE_FREE = 5


class BeveragesGlass(Enum):
    BEER_GLASS = 1
    RED_WINE_GLASS = 2
    WHITE_WINE_GLASS = 3
    VODKA_GLASS = 4
    WHISKEY_GLASS = 6
    TEQUILA_GLASS = 8
    CAMPARI_GLASS = 10
    ARAK_GLASS = 12
    GIN_GLASS = 14


class BeveragesChaser(Enum):
    VODKA_CHASER = 5
    WHISKEY_CHASER = 7
    TEQUILA_CHASER = 9
    CAMPARI_CHASER = 11
    ARAK_CHASER = 13
    GIN_CHASER = 15


class KindOfMeal(Enum):
    MEAT = 1
    DAIRY = 2


class EventState(Enum):
    GENERATING = 1
    IN_PROGRESS = 2
    FINISHED = 3


EQUIPMENT_LIST_FILE_TEMPLATE = "files/{}_equipment_list.json"
