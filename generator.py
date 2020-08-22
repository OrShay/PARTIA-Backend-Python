import json
import math
from equipment_list import EquipmentList
from constants import *


def _add_simple_items_to_dict(equipment_list: EquipmentList, new_items_info: list):
    """
    This function gets a dictionary of items and info of new items,
    creates new items and adds each of them to the dictionary
    :param items_dict:<name>:<Item>
    :param new_items_info: json with list of simple items (the amount is 1)
    """
    for title in new_items_info:
        try:
            equipment_list.add_new_item(title, 1)
        except Exception as ex:
            print(f"Could not add {title} to the list because {ex}")


def _add_complex_items_to_dict(equipment_list: EquipmentList, new_items_info: dict, num_of_participants):
    for title in new_items_info.keys():
        amount = math.ceil(new_items_info[title] * num_of_participants)
        try:
            equipment_list.add_new_item(title, amount)
        except Exception as ex:
            print(f"Could not add {title} to the list because {ex}")


def _add_simple_items_from_file_to_dict(equipment_list: EquipmentList, file_prefix):
    file_name = EQUIPMENT_LIST_FILE_TEMPLATE.format(file_prefix)
    with open(file_name) as json_file:
        data = json.load(json_file)
    _add_simple_items_to_dict(equipment_list, data["EquipmentList"])


def _add_meat_meal_items(equipment_list: EquipmentList, food_info_json, num_of_participants, preferences_sum):
    _add_simple_items_to_dict(equipment_list, food_info_json["equipment"])
    _add_complex_items_to_dict(equipment_list, food_info_json["general"], num_of_participants)
    num_of_vegetarian = preferences_sum[FoodPreference.VEGETARIAN.name]
    num_of_vegan = preferences_sum[FoodPreference.VEGAN.name]
    num_of_meat_eaters = num_of_participants - num_of_vegan - num_of_vegetarian
    _add_complex_items_to_dict(equipment_list, food_info_json["meat"], num_of_meat_eaters)
    num_of_participants_after_veggie_ratio = num_of_participants + 0.2 * (num_of_vegetarian + num_of_vegan)
    _add_complex_items_to_dict(equipment_list, food_info_json["vegetarian"], num_of_participants_after_veggie_ratio)


def _add_dairy_meal_items(equipment_list: EquipmentList, food_info_json, num_of_participants, preferences_sum):
    _add_simple_items_to_dict(equipment_list, food_info_json["equipment"])
    _add_complex_items_to_dict(equipment_list, food_info_json["food"], num_of_participants)


def _add_alcohol_shots_and_glasses_items_by_ratio(equipment_list: EquipmentList, drinks_json, preferences_sum):
    drinks_list = drinks_json["drinks_list"]
    shot_ratio = drinks_json["shot_amount"]
    glass_ratio = drinks_json["glass_amount"]
    for drink in drinks_list:
        amount = preferences_sum[f"{drink.upper()}_SHOTS"] * shot_ratio
        amount += preferences_sum[f"{drink.upper()}_GLASS"] * glass_ratio
        equipment_list.add_new_item(drink, amount)


def _add_alcohol_bottles_items_by_ratio(equipment_list: EquipmentList, alcohol_info, preference_sum):
    for drink in alcohol_info:
        amount = preference_sum[drink] * alcohol_info[drink]
        equipment_list.add_new_item(drink, amount)


def generate_alcohol_items_dict(equipment_list: EquipmentList, num_of_participants, preference_sum):
    with open("files/AlcoholJson.json") as json_file:
        alcohol_json_info = json.load(json_file)
    _add_alcohol_shots_and_glasses_items_by_ratio(equipment_list, alcohol_json_info["Drinks"], preference_sum)
    _add_alcohol_bottles_items_by_ratio(equipment_list, alcohol_json_info["Bottles"], preference_sum)


def generate_food_items_dict(equipment_list: EquipmentList, kind_of_meal: str, num_of_participants, preferences_sum):
    with open("files/FoodJson.json") as json_file:
        food_json_info = json.load(json_file)
    if kind_of_meal == "MEAT":
        _add_meat_meal_items(equipment_list, food_json_info["MEAT"], num_of_participants, preferences_sum)
    elif kind_of_meal == "DAIRY":
        _add_dairy_meal_items(equipment_list, food_json_info["DAIRY"], num_of_participants, preferences_sum)


def generate_equipment_list(equipment_list: EquipmentList, kind_of_event: str, environment: str):
    """
    This function gets the kind of event and environment and reads the relevant files,
    and generates an equipment list
    :param kind_of_event: {"BACHELORETTE", "BIRTHDAY", "GATHERING"}
    :param environment: {"OUTDOORS", "INDOORS"}
    :return: a dictionary of items and bool
    """
    _add_simple_items_from_file_to_dict(equipment_list, kind_of_event)
    _add_simple_items_from_file_to_dict(equipment_list, environment)


