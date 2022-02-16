import logging
from Db_config import local_session, create_all_entities
from DbRepo import DbRepo
from AirlineCompany import AirlineCompany
from Flight import Flight
from Country import Country
from BaseFacade import BaseFacade
from UsernotauthorizedException import UsernotauthorizedException
from Logger import *

class AirLineFacade(BaseFacade):

    def __init__(self, logintoken):
        super().__init__(logintoken)
        #self.repo=DbRepo(local_session)
        #self.logintoken = logintoken


    def get_my_flights(self): #by id
        self.logger.logger.debug( f'get flight by airline, for airline company id  {self.logintoken}'
                                              f' is about to happen')
        flights= self.repo.get_by_id(Flight,(self.logintoken.id))
        self.logger.logger.info( f'--SUCCESS--  get flights by airline company {self.logintoken.name}  id '
                       f' {self.logintoken.id} is finish Successfully')
        return flights


    def update_airline(self,airline): #update by object. #if i dont update some field, he gets None
        self.repo.print_to_log(logging.DEBUG, f'update airline is about to happen')
        if airline.id!=self.logintoken.id:
            raise UsernotauthorizedException
        # trying to find this airline in Airline Company, and to check if there isnt another airline company
        # with this deatils:
        # Name
        if self.repo.get_by_condition(AirlineCompany, lambda query: query.filter(
                AirlineCompany.name == airline.name).all()):
            print('Failed, a airline company with this name  is already exists.')
            self.repo.print_to_log(logging.ERROR,
                                       f'--FAILED--  update by  airline id  {airline.id} '
                                       f'failed because  airline company  name  {airline.name}'
                                       f'is alredy exists.')
            return False
        self.repo.update_by_id(AirlineCompany, airline.id,
                                   {AirlineCompany.name: airline.name, AirlineCompany.country_id: airline.country_id})
        self.repo.print_to_log(logging.INFO,
                                   f'--Sucsses--  Airline id  {airline.id}  update details:'
                                   f' {airline}')


    def add_flight(self, flight):#flight is object with airline company id
        self.repo.print_to_log(logging.DEBUG, f'add new flight for airline company {self.logintoken.name}'
                                              f' id {self.logintoken.id} is about to happen')
        if flight.airline_Company_Id != self.logintoken.id:
            raise UsernotauthorizedException
        elif not self.repo.get_by_condition(Country,
                                            lambda query: query.filter(Country.id == flight.origin_Country_id).all()):
            print('Failed, This origin country did not exist in our country DB')
            self.repo.print_to_log(logging.ERROR,
                                   f'--FAILED--  update by  flight id  {flight.id} '
                                   f'failed because  the origin country {flight.origin_Country_id} did not exist in'
                                   f' our country DB')
            return False
        elif not self.repo.get_by_condition(Country,
                                            lambda query: query.filter(
                                                Country.id == flight.destination_Country_id).all()):
            print('Failed, This destination country did not exist in our country DB')
            self.repo.print_to_log(logging.ERROR,
                                   f'--FAILED--  update by  flight id  {flight.id} '
                                   f'failed because  the destination country {flight.destination_Country_id} did not exist in'
                                   f' our country DB')
            return False
        elif flight.origin_Country_id == flight.destination_Country_id:
            print('Failed, This destination country id and origin country id cant be the same.')
            self.repo.print_to_log(logging.ERROR,
                                   f'--FAILED--  update by  flight id  {flight.id} '
                                   f'failed because  this destination country id  {flight.destination_Country_id}'
                                   f'and origin country id cant be the same')
            return False
        if flight.departure_Time > flight.landing_Time:
            print(f' flight cant landing before departure')
            self.repo.print_to_log(logging.ERROR,
                              f'--FAILED--  update by  flight id  {flight.id} '
                               f'failed because  flight cant landing before departure. '
                               f' departure time: {flight.departure_Time} ,landing time: {flight.landing_Time}')
            return False
        if flight.remaining_Tickets <= 0:
            print(f' at least 0 ticket for flight. remaining tickets need to be positive')
            self.repo.print_to_log(logging.ERROR,
                              f'--FAILED--  remaining tickets = {flight.remaining_Tickets}, need to be positive '
                               f' at least 0 ticket for flight')
            return False
        else:
            self.repo.add(flight)
            return


    def update_flight(self, flight): #flight is object with airline company id
        if flight.airline_Company_Id != self.logintoken.id:
            raise UsernotauthorizedException
        else:
            self.repo.print_to_log(logging.DEBUG, f'update flight number {flight.id} is about to happen')
            flight_=self.repo.get_by_condition(Flight, lambda query: query.filter(Flight.id == flight.id).all())
            if not flight_:
                print('Failed, we cant find this flight.')
                self.repo.print_to_log(logging.ERROR,
                                       f'--FAILED--  we cant find flight number  {flight.id} ')
                return False
            elif not self.repo.get_by_condition(Country,
                                        lambda query: query.filter(Country.id == flight.origin_Country_id).all()):
                print('Failed, This origin country did not exist in our country DB')
                self.repo.print_to_log(logging.ERROR,
                                       f'--FAILED--  update by  flight id  {flight.id} '
                                       f'failed because  the origin country {flight.origin_Country_id} did not exist in'
                                       f' our country DB')
                return False
            elif not self.repo.get_by_condition(Country,
                                           lambda query: query.filter(Country.id == flight.destination_Country_id).all()):
                print('Failed, This destination country did not exist in our country DB')
                self.repo.print_to_log(logging.ERROR,
                                       f'--FAILED--  update by  flight id  {flight.id} '
                                       f'failed because  the destination country {flight.destination_Country_id} did not exist in'
                                       f' our country DB')
                return False
            elif flight.origin_Country_id == flight.destination_Country_id:
                print('Failed, This destination country id and origin country id cant be the same.')
                self.repo.print_to_log(logging.ERROR,
                                       f'--FAILED--  update by  flight id  {flight.id} '
                                       f'failed because  this destination country id  {flight.destination_Country_id}'
                                       f'and origin country id cant be the same')
                return False
            elif flight.departure_Time >= flight_[0].landing_Time:
                print(f' flight cant landing before departure')
                self.repo.print_to_log(logging.ERROR,
                                   f'--FAILED--  update by  flight id  {flight.id} '
                                   f'failed because  flight cant landing before departure. '
                                   f' departure time: {flight.departure_Time} ,landing time: {flight.landing_Time}')
                return False
            elif flight[0].remaining_Tickets < 0:
                print(f' at least 0 ticket for flight. remaining tickets need to be positive')
                self.repo.print_to_log(logging.ERROR,
                                       f'--FAILED--  remaining tickets = {flight.remaining_Tickets}, need to be positive '
                                       f' at least 0 ticket for flight')
                return False
            else:
                self.repo.update_by_id(Flight, flight.id, flight,
                                       {Flight.origin_Country_id: flight.origin_Country_id,
                                        Flight.destination_Country_id: flight.destination_Country_id,
                                        Flight.departure_Time: flight.departure_Time,
                                        Flight.landing_Time: flight.landing_Time,
                                        Flight.remaining_Tickets: flight.remaining_Tickets})
                self.repo.print_to_log(logging.INFO,
                                       f'--Sucsses--  flight id  {flight.id}  update details:'
                                       f' {flight}')


    def remove_flight(self, airline_id, flight_id): #remove by flight id
        self.repo.print_to_log(logging.DEBUG, f'remove flight is about to happen')
        if not self.repo.get_by_condition(Flight,
                                              lambda query: query.filter(Flight.id == flight_id).all()):
            print(f'Failed, we cant find  flight number {flight_id}')
            self.repo.print_to_log(logging.ERROR,
                                   f'--FAILED--    we cant find  flight number {flight_id}')
            return False
        elif self.logintoken.role != 3:
            if airline_id != self.logintoken.id:
                raise UsernotauthorizedException
        self.repo.delete(Flight, flight_id)
        self.repo.print_to_log(logging.INFO,
                                   f'--Sucsses--  flight  id {flight_id} is removed')
        return True
