#need to adding token+ check the uptade func.
import logging
from Db_config import local_session, create_all_entities
from DbRepo import DbRepo
from AirlineCompany import AirlineCompany
from Administrator import Administrator
from Flight import Flight
from Customer import Customer
from LoginToken import LoginToken
from Country import Country
from BaseFacade import BaseFacade

class AirLineFacade(BaseFacade):

    def __init__(self, logintoken):
        self.repo=DbRepo(local_session)
        self.logintoken = logintoken


    def get_flights_by_airline(self, airline_id): #buy id
        self.repo.print_to_log(logging.INFO, f'get flight by airline, for airline company id  {airline_id} is about to happen')
        return self.repo.getFlightsByAirlineId(airline_id)


    def update_airline(self, airline): #update by object.
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


    def update_flight(self, flight_id, data): #check with object  #DIDNT WORK
        # #need to check if the flight is of the airline co with the token
            self.repo.print_to_log(logging.DEBUG, f'update flight is about to happen')
            flight_=self.repo.get_by_condition(Flight, lambda query: query.filter(Flight.id == flight_id).all())
            if not flight_:
                print('Failed, we cant find this flight.')
                self.repo.print_to_log(logging.ERROR,
                                       f'--FAILED--  we cant find flight number  {flight.id} ')
                return
            if not self.repo.get_by_condition(Country,
                                        lambda query: query.filter(Country.id == data.origin_Country_id).all()):
                print('Failed, This origin country did not exist in our country DB')
                self.repo.print_to_log(logging.ERROR,
                                       f'--FAILED--  update by  flight id  {flight_id} '
                                       f'failed because  the origin country {data.origin_Country_id} did not exist in'
                                       f' our country DB')
            elif not self.repo.get_by_condition(Country,
                                           lambda query: query.filter(Country.id == data.destination_Country_id).all()):
                print('Failed, This destination country did not exist in our country DB')
                self.repo.print_to_log(logging.ERROR,
                                       f'--FAILED--  update by  flight id  {flight_id} '
                                       f'failed because  the destination country {data.destination_Country_id} did not exist in'
                                       f' our country DB')
            elif data.departure_Time >= flight_[0].landing_Time:
                print(f' flight cant landing before departure')
                self.repo.print_to_log(logging.ERROR,
                                   f'--FAILED--  update by  flight id  {flight.id} '
                                   f'failed because  flight cant landing before departure. '
                                   f' departure time: {flight.departure_Time} ,landing time: {flight.landing_Time}')
            elif flight(0).remaining_Tickets < 0:
                print('you cant update minus remaining tickets')
            else:
                self.repo.update_by_id(Flight, flight.id, flight)
                                       #{Flight.origin_Country_id: flight.origin_Country_id,
                                        #Flight.destination_Country_id: flight.destination_Country_id,
                                        #Flight.departure_Time: flight.departure_Time,
                                        #Flight.landing_Time: flight.landing_Time,
                                        #Flight.remaining_Tickets: flight.remaining_Tickets})
                self.repo.print_to_log(logging.INFO,
                                       f'--Sucsses--  flight id  {flight.id}  update details:'
                                       f' {flight}')


