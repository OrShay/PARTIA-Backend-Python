from participant import Participant
from ride import Ride


class RidesBoard:
    def __init__(self):
        self._rides = set()

    def add_ride(self, driver: Participant, available_seats: int, source: str, departure_time=None):
        new_ride = Ride(driver, available_seats, source, departure_time)
        self._rides.add(new_ride)

    def remove_ride(self, ride_to_remove: Ride):
        self._rides.remove(ride_to_remove)

    def get_rides(self):
        return self._rides
