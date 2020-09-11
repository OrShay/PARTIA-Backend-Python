from dateutil import parser
from rides_board import RidesBoard
from participant import Participant
from cashier import Cashier
from equipment_list import EquipmentList
from generator import generate_equipment_list, generate_food_items_dict, generate_alcohol_items_dict
from constants import EventState, Beverages, KindOfMeal, KindOfEvent, FoodPreference


class Event:
    _event_counter = 1

    def __init__(self, event_info_dict):
        self._pin_code = Event._event_counter
        self.state = EventState.GENERATING.name
        Event._event_counter += 1
        try:
            self._create_event_from_dict(event_info_dict)
        except KeyError:
            raise
        self.participants_dict = {}
        self.rides_board = RidesBoard()
        self.cashier = Cashier()
        self.equipment_list = EquipmentList()
        self.kind_Of_Meal = None
        self.participants_preferences_sum = {preference: 0 for preference in
                                             set(FoodPreference.__members__.keys()).union(Beverages.__members__.keys())}

    def get_pin_code(self):
        return self._pin_code

    def set_date(self, date):
        self.date_time = date

    def _create_event_from_dict(self, event_info_dict: dict):
        try:
            self.name = event_info_dict.get("name", "NewEvent")
            self.location = event_info_dict.get("location", "To Be Decided")
            self.info = event_info_dict.get("info", "")
            self.environment = event_info_dict["environment"]
            self.kind_of_event = event_info_dict["kind_of_event"]
            self.date_time = parser.parse(event_info_dict["date"])
            self.meal_organization = event_info_dict["meal_organization"]
            self.beverage_organization = event_info_dict["beverage_organization"]
            self.owner = event_info_dict["owner"]
        except KeyError as e:
            print(f"Error while trying to create new event. {e}")
            raise

    def _add_participant_preference_to_sum(self, participant_preferences):
        """
        This function adds a participant's preferences to the total of preferences of the event
        :return:
        """
        for preference in self.participants_preferences_sum.keys():
            if participant_preferences[preference]:
                self.participants_preferences_sum[preference] += 1

    def set_kind_of_meal(self, kind_of_meal: str):
        """
        This function gets a kind of meal
        :param kind_of_meal: string
        :return: True iff set successfully
        """
        if kind_of_meal in KindOfMeal.__members__.keys():
            self.kind_Of_Meal = kind_of_meal
            return True
        else:
            return False

    def get_food_statistics(self):
        """
        This function calculates the food preferences statistics
        :return: dictionary of- <food_preference>:<the_ratio>
        """
        num_of_participants = len(self.participants_dict)
        food_statistics = {preference: self.participants_preferences_sum[preference] / num_of_participants
                           for preference in FoodPreference.__members__.keys()}
        return food_statistics

    def get_beverages_statistics(self):
        """
        This function calculates the beverages preferences statistics
        :return: dictionary of- <beverage_preference(str)>:<the_ratio(float)>
        """
        num_of_participant = len(self.participants_dict)
        beverages_statistics = {preference: self.participants_preferences_sum[preference] / num_of_participant
                                for preference in Beverages.__members__.keys()}
        return beverages_statistics

    def add_participant(self, user_name: str, preference_answers: dict):
        if user_name in self.participants_dict.keys():
            return False
        else:
            new_participant = Participant(user_name, preference_answers)
            self.participants_dict[user_name] = new_participant
            self._add_participant_preference_to_sum(preference_answers)
            return True

    def get_equipment_list(self, regenerate=False):
        if self.state == EventState.GENERATING.name or regenerate:
            self._generate_equipment_list()
            self.state = EventState.IN_PROGRESS
        return self.equipment_list.items

    def _generate_equipment_list(self):
        generate_equipment_list(self.equipment_list, self.kind_of_event, self.environment)
        if self.meal_organization:
            generate_food_items_dict(self.equipment_list, self.kind_Of_Meal, len(self.participants_dict),
                                     self.participants_preferences_sum)
        if self.beverage_organization:
            generate_alcohol_items_dict(self.equipment_list, len(self.participants_dict),
                                        self.participants_preferences_sum)

    def is_event_participant(self, username):
        return username in self.participants_dict.keys()

    def is_event_owner(self, user_name: str):
        """
        This function returns true iff the user_name is the owner of the event
        """
        return self.owner == user_name

    def get_event_info(self):
        return {"pin_code": self._pin_code,
                "owner": self.owner,
                "name": self.name,
                "location": self.location,
                "info": self.info,
                "date": self.date_time,
                "state": self.state}

    def set_item_price(self, title, price, who_paid):
        participant = self.participants_dict.get(who_paid)
        if not participant:
            raise ValueError('Invalid username')
        self.get_equipment_list()
        self.equipment_list.set_item_price(title, price, participant)
        self.cashier.add_money_spent(price)

    def remove_item(self, title):
        self.get_equipment_list()
        price = self.equipment_list.remove_item(title)
        self.cashier.decrease_money_spent(price)

    def split_investment(self):
        return self.cashier.split_payment(self.participants_dict)