from participant.participant import Participant


class Cashier:
    def __init__(self):
        self._money_spent = 0

    def get_money_spent(self):
        return self._money_spent

    def add_money_spent(self, value_spent):
        self._money_spent += value_spent

    def decrease_money_spent(self, money_value):
        self._money_spent -= money_value
        self._money_spent = 0 if self._money_spent < 0 else self._money_spent

    def split_payment(self, participants_dict: {str: Participant}):
        """
        This function gets a participants dict, and creates a payment dict,
        for each participant (user_name) the amount she owes.
        :param participants_dict:
        :return: {user_name : money_owes}
        """
        payment_participants_owe = {}
        total_payment_for_each = self._money_spent / len(participants_dict)
        for user_name in participants_dict:
            owes = total_payment_for_each - participants_dict[user_name].get_investment()
            payment_participants_owe[user_name] = owes
        return payment_participants_owe
