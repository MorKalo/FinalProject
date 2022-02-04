from BaseFacade import BaseFacade
from Db_config import local_session, create_all_entities
from DbRepo import DbRepo
from AirlineCompany import AirlineCompany
from Administrator import Administrator
from Flight import Flight
from Customer import Customer

class AirLineFacade(BaseFacade):

    def __init__(self, token):
        self.repo=DbRepo(local_session)
        self.token=token

    def get_flights_by_airline(self, airline):
        print(self.repo.getFlightsByAirlineId(airline))


    def update_airline(self, airline_id, data):
        self.repo.update(AirlineCompany, airline_id, data)

    def update_flight(self, flight_id, data):
        self.repo.update(Flight, flight_id, data)




