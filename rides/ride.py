from json import JSONEncoder
from participant.participant import Participant
from datetime import datetime


class Ride:
    def __init__(self, driver: Participant, total_seats: int, source: str, departue_time):
        self._driver = driver
        self._passengers = []
        self._available_seats = total_seats
        self._source = source
        self._departure_time = departue_time

    def set_available_seats(self, available_seats: int):
        self._available_seats = available_seats

    def get_available_seats(self):
        return self._available_seats

    def set_source(self, source: str):
        self._source = source

    def get_source(self):
        return self._source

    def set_departure_time(self, departure_time: datetime):
        self._departure_time = departure_time

    def get_departure_time(self):
        return self._departure_time

    def get_passengers_names(self):
        return [passenger.get_username() for passenger in self._passengers]

    def add_passenger(self, passenger: Participant):
        if len(self._passengers) < self._available_seats:
            self._passengers.append(passenger)
            self._available_seats = self._available_seats - 1
        else:
            raise Exception("No available seats")  # Todo: change to custom exception

    def remove_passenger(self, passenger: Participant):
        if passenger in self._passengers:
            self._passengers.remove(passenger)
            self._available_seats = self._available_seats + 1

    def get_driver(self):
        return self._driver


class RideEncoder(JSONEncoder):

    def default(self, ride):
        if isinstance(ride, Ride):
            json = {"driver_name": ride.get_driver().get_username(),
                    "passengers": ride.get_passengers_names(),
                    "available_seats": ride.get_available_seats(),
                    "source": ride.get_source(),
                    "departure_time": ride.get_departure_time()
                    }
            return json
        else:
            # call base class implementation which takes care of
            # raising exceptions for unsupported types
            return JSONEncoder.default(self, ride)
