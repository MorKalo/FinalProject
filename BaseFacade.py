#NEED TO FINISH: i need to add func get customer?
import logging
from DbRepo import DbRepo
from Db_config import local_session, create_all_entities
from abc import ABC, abstractmethod
from Flight import Flight
from AirlineCompany import AirlineCompany
from Country import Country
from User import User
from UserAlreadyExistException import UserAlreadyExistException
from Logger import Logger
from LoginToken import LoginToken
repo = DbRepo(local_session)


class BaseFacade(ABC):

    @abstractmethod
    def __init__(self, logintoken = LoginToken(id=None, name='Anonymous', role=4)):
        #self.repo=repo
        self.logger = Logger.get_instance()
        self.repo = DbRepo(local_session)
        self.logintoken = logintoken

    def get_all_flights(self):
        print(self.repo.get_all(Flight))


    def get_flight_by_id(self, id):
        if not isinstance(id, int):
            print('You must insert integer for ID.')
            return
        if id<=0:
            print('ID must be positive.')
            return
        return self.repo.get_by_id(Flight, id)


    def get_flight_by_parameters(self, origin_country_id, destination_country_id, date):
        if not isinstance(origin_country_id, int) or not isinstance(destination_country_id, int):
            print('Origin country id and destination country id need to be integer')
            return
        if origin_country_id<=0 or destination_country_id<=0 :
            print('Origin country id and destination country id need to be positive')
            return
        return \
            self.repo.getFlightsByOriginCountryId(origin_country_id) and \
            self.repo.getFlightsByDestinationCountryId(destination_country_id) and \
            self.repo.getFlightsByDepartureDate(date)


    def get_all_airlines(self):
        print(self.repo.get_all(AirlineCompany))


    def get_airline_by_id(self, id):
        return self.repo.get_by_id(AirlineCompany, id)

    def add_user(self, user):
         self.repo.add(user)


    def add_customer(self, customer):
        return self.repo.add(customer)


    def add_airline(self, airline) :
         self.repo.add(airline)


    def get_all_countries(self):
        print(self.repo.get_all(Country))


    def get_country_by_id(self, id):
        print(self.repo.get_by_id(Country, id))


    def create_new_user(self, user):
        username=self.repo.get_by_condition(User, lambda query: query.filter(User.username == user.username).all())
        if username:
            self.repo.print_to_log(logging.ERROR,
                                   f'--FAILED--   The username "{username[0].username}"  is alrady exist ')
            raise UserAlreadyExistException()
        else:
            email=self.repo.get_by_condition(User, lambda query: query.filter(User.email == user.email).all())
            if email:
                print(f' Faild, the email {email[0].email} is alrady exist ')
                self.repo.print_to_log(logging.ERROR,
                                       f'--FAILED--   The email "{email[0].email}"  is alrady exist ')
            self.repo.add(user)
            self.repo.print_to_log(logging.INFO,
            f'--Sucsses-- the user "{user.username}"  was created successfully, his details:   user id:{user.id} email:{user.email}, user role:{user.user_role}  ')
            return True









    def __repr__(self):
        return f'\n<id={self.id} n >'

    def __str__(self):
        return f'\n<id={self.id} n >'

