import logging
from BaseFacade import BaseFacade
from Db_config import local_session, create_all_entities
from DbRepo import DbRepo
from AirlineCompany import AirlineCompany
from Administrator import Administrator
from Flight import Flight
from Customer import Customer
from AnonymusFacade import AnonymusFacade
from LoginToken import LoginToken

class AirLineFacade(AnonymusFacade):

    def __init__(self, token):
        self.repo=DbRepo(local_session)
        self.token =token


    def get_flights_by_airline(self, airline_id): #buy id
        self.repo.print_to_log(logging.INFO, f'get flight by airline, for airline company id  {airline_id} is about to happen')
        return self.repo.getFlightsByAirlineId(airline_id)


    def update_airline(self, airline): # need to add the token
        self.repo.print_to_log(logging.DEBUG, f'update airline is about to happen')
        #no need to check if the airline company is exists because the TOKEN.
        # trying to find this airline in Airline Company, and to check if there isnt another airline company with does deatils:
        # Name
        if self.repo.get_by_condition(AirlineCompany, lambda query: query.filter(
                AirlineCompany.name == airline.name).all()):
            print('Failed, a airline company with this name  is already exists.')
            self.repo.print_to_log(logging.ERROR,
                                       f'--FAILED--  update by  airline id  {airline.id} '
                                       f'failed because  airline company  name  {airline.name}'
                                       f'is alredy exists.')
            return
        self.repo.update_by_id(AirlineCompany, airline.id,
                                   {AirlineCompany.name: airline.name, AirlineCompany.country_id: airline.country_id})
        self.repo.print_to_log(logging.INFO,
                                   f'--Sucsses--  Airline id  {airline.id}  update details:'
                                   f' {airline}')






    def update_flight(self, flight_id, data):
        self.repo.update(Flight, flight_id, data)




