from equipment.item import Item
from participant.participant import Participant


class EquipmentList:
    def __init__(self):
        self.items = {}

    def add_new_item(self, name, amount: int):
        """
        this function gets name and amount of new item, creates new item and
        adds it to the items dict {name: Item},
        The name must be unique, if this name already exists the method raises exception
        :param name: Item title
        :param amount: Item quantity
        """
        if name in self.items.keys():
            raise Exception("There is already an item in that name")
        else:
            new_item = Item(name, amount)
            self.items[name] = new_item

    def get_an_item(self, name):
        """
        This function gets a name of an item and returns iy if exists
        :param name: title of an Item
        :return: Item if exists None otherwise
        """
        self.items.get(name, None)

    def set_item_price(self, name, price: float, who_paid: Participant):
        try:
            item_to_update = self.items[name]
            item_to_update.set_price(price=price, who_paid=who_paid)
        except KeyError:
            raise NameError("There is no item that name")

    def add_in_charge(self, item_name, participant_in_charge, amount):
        try:
            item_to_update = self.items[item_name]
            item_to_update.add_in_charge(participant_in_charge, amount)
        except KeyError as ex:
            raise NameError("There is no item that name")

    def remove_in_charge(self, item_name, participant_in_charge):
        try:
            item_to_update = self.items[item_name]
            item_to_update.remove_in_charge(participant_in_charge)
        except KeyError:
            raise NameError("There is no item that name")
        except ValueError:
            raise

    def update_item_in_charge(self, item_name, participant_in_charge, new_amount):
        try:
            item_to_update = self.items[item_name]
            item_to_update.update_in_charge(participant_in_charge, new_amount)
        except KeyError:
            raise NameError("There is no item that name")
        except ValueError:
            raise

    def set_item_amount(self, item_name, amount):
        try:
            item_to_update = self.items[item_name]
            item_to_update.set_amount(amount)
        except KeyError:
            raise NameError("There is no item that name")
        except ValueError:
            raise

    def remove_item(self, item_name):
        if item_name not in self.items.keys():
            raise ValueError("There is no item that name")
        item = self.items[item_name]
        price = item.total_price
        self.items.pop(item_name)
        return price
