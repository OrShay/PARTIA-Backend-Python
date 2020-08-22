from participant import Participant
from json import JSONEncoder


class Item:
    def __init__(self, title: str, amount: float):
        self.title = title
        self.amount = amount
        self.left_to_bring = amount
        self.total_price = 0
        self.in_charge = {}     # Participant: float

    def set_price(self, price: float, who_paid: Participant):
        self.total_price += price
        who_paid.increase_investment(price)

    def add_in_charge(self, participant_in_charge, amount):
        """
        this function gets participant to add to "in-charge" list, and amount of products she's bringing
        :param participant_in_charge: The participant which gets the item
        :param amount: amount of item the participant gets
        :return: Raises exception if there is no need to bring as much
        """
        if self.left_to_bring < amount:
            raise ValueError("There is no need to bring this item")
        else:
            self.left_to_bring -= amount
            self.in_charge[participant_in_charge] = amount

    def remove_in_charge(self, participant_to_remove):
        if participant_to_remove in self.in_charge.keys():
            amount_to_add = self.in_charge[participant_to_remove]
            self.in_charge.pop(participant_to_remove)
            self.left_to_bring += amount_to_add
        else:
            raise ValueError("This participant is not in charge")

    def update_in_charge(self, participant_to_update, new_amount):
        if participant_to_update in self.in_charge.keys():
            left_to_bring = self.left_to_bring + self.in_charge[participant_to_update]
            if new_amount <= left_to_bring:
                self.left_to_bring = left_to_bring
                self.in_charge[participant_to_update] = new_amount
            else:
                raise ValueError("There is no need to bring that much")
        else:
            raise ValueError("This participant is not in charge")

    def set_amount(self, new_amount):
        # increase amount
        if self.amount <= new_amount:
            self.amount = new_amount
        # decrease amount
        elif self.amount - self.left_to_bring <= new_amount:
            self.left_to_bring -= self.amount - new_amount
            self.amount = new_amount
        else:
            raise ValueError("There are participants in charge of the more than the new amount")


class ItemEncoder(JSONEncoder):

    def default(self, item):
        if isinstance(item, Item):
            json = {"title": item.title,
                    "amount": item.amount,
                    "left_to_bring": item.left_to_bring,
                    "total_price": item.total_price,
                    "in_charge": None
                    }
            if len(item.in_charge.keys()) > 0:
                json["in_charge"] = {participant.get_username(): amount for participant, amount in item.in_charge.items()}
            return json

        else:
            # call base class implementation which takes care of
            # raising exceptions for unsupported types
            return JSONEncoder.default(self, item)
