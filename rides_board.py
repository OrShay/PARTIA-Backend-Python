from participant import Participant
from ride import Ride


class RidesBoard:
    def __init__(self):
        self._rides = {}  # dictionary of <driver_name : ride>

    def add_ride(self, driver: Participant, available_seats: int, source: str, departure_time=None):
        new_ride = Ride(driver, available_seats, source, departure_time)
        self._rides[driver.get_username()] = new_ride

    def remove_ride(self, driver: str):
        try:
            self._rides.pop(driver)
        except KeyError:
            raise KeyError("Invalid driver name")

    def get_rides(self):
        return self._rides
