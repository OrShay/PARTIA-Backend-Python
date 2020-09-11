import json
from event import Event


class AppEngine:
    events_dict = {}
    users_dict = {}

    @staticmethod
    def create_new_event(event_creation_info: json):
        """
        This function creates new event and saves it in the events dictionary
        :param event_creation_info: a json with info about the new event to create
        :return: pin code of the new event, None if error occurred
        """
        try:
            new_event = Event(event_creation_info)
            pin_code = new_event.get_pin_code()
            AppEngine.events_dict[pin_code] = new_event
            return pin_code
        except KeyError:
            raise

    @staticmethod
    def get_event_by_pin_code(pin_code: int):
        """
        This function returns an Event object by its uuid pin code
        :param pin_code: the unique pin code of the event
        :return: Event object or None if does not exist
        """
        event = AppEngine.events_dict.get(pin_code, None)
        return event

    @staticmethod
    def is_logged_user(user_name, password):
        if user_name in AppEngine.users_dict.keys():
            if AppEngine.users_dict[user_name] == password:
                return True
            else:
                return False

    @staticmethod
    def signup_new_user(username, password):
        if username in AppEngine.users_dict.keys():
            return False
        AppEngine.users_dict[username] = password
        return True

    @staticmethod
    def get_user_events(username):
        events_dict = {
            "owner": [],
            "participates": []
        }
        if username not in AppEngine.users_dict.keys():
            raise NameError
        for event in AppEngine.events_dict.values():
            if event.is_event_participant(username):
                if event.is_event_owner(username):
                    events_dict["owner"].append(event.get_event_info())
                else:
                    events_dict["participates"].append(event.get_event_info())
        return events_dict
