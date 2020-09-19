class Participant:
    """
        This class represent a participant of the event
 """

    def __init__(self, name: str, food_preference, allergies, glass_preference, chaser_preference):
        self._username = name  # as shown in partia_app
        self._food_preference = food_preference
        self._allergies = allergies
        self._glass_preference = glass_preference
        self._chaser_preference = chaser_preference
        self._investment = float()  # how much spent so far

    def increase_investment(self, sum_to_add: float):
        self._investment = self._investment + sum_to_add

    def get_username(self):
        return self._username

    def get_investment(self):
        return self._investment

    def get_food_preference(self):
        return self._food_preference

    def get_allergies(self):
        return self._allergies

    def get_glass_preference(self):
        return self._glass_preference

    def get_chaser_preference(self):
        return self._chaser_preference
