import logging
from BaseFacade import BaseFacade
from Db_config import local_session, create_all_entities
from DbRepo import DbRepo
from Administrator import Administrator
from Customer import Customer
from AirlineCompany import AirlineCompany
from User import User
from Country import Country
from LoginToken import LoginToken
from AnonymusFacade import AnonymusFacade


class AdministratorFacade(BaseFacade):

    def __init__(self):
        self.repo=DbRepo(local_session)
        #self.token=token

    def get_all_customers(self):#finish and check
        self.repo.print_to_log(logging.DEBUG, f'get all customer"s is about to happen')
        return self.repo.get_all(Customer)

    def create_airline(self, user, airline):#user and airline are object
        annfacade=AnonymusFacade()
        if annfacade.create_new_user(user):
            self.add_airline(user, airline)
            self.repo.print_to_log(logging.INFO,
                           f'--Sucsses--  User created: {user}, Airline created: {airline}')
        else:
            print (f'--Failed-- we cant create this user and airline company')
            self.repo.print_to_log(logging.ERROR,
                                   f'--FAILED--   we cant create this user and airline company .')



    def add_airline(self, user, airline):#use this func from create airline only.
        self.repo.print_to_log(logging.DEBUG, f'add new airline is about to happen')
        if user.user_role!=1:
            print('Failed. User role need to be "AIRLINE".')
            self.repo.print_to_log(logging.ERROR,
                                   f'--FAILED--   User role need to be "AIRLINE" but we get {user.user_role} .')
            return
        if  self.repo.get_by_condition(AirlineCompany, lambda query: query.filter(
                        AirlineCompany.name == airline.name).all()):
            print('Failed.  we already have Airline company with this name.')
            self.repo.print_to_log(logging.ERROR,
                        f'--FAILED--  {airline.name} we already have Airline company with this name')
            return
        if not self.repo.get_by_condition(Country,
                                          lambda query: query.filter(Country.id == airline.country_id).all()):
            print(f' Failed.  the country {airline.country_id} does not exist.')
            return
        airline.user_id=user.id
        self.repo.add(airline)
        return


    def add_user(self, user):            # NEED TO DO EXCEPTION UserAlreadyExistException
        self.repo.print_to_log(logging.DEBUG, f'add new airline is about to happen')
        email = self.repo.get_by_condition(User, lambda query: query.filter(User.email == user.email).all())
        username = self.repo.get_by_condition(User, lambda query: query.filter(User.username == user.username).all())
        self.repo.print_to_log(logging.DEBUG, f'check details for user first')
        if email:
            print('Failed.  we already have user with this Email.')
            self.repo.print_to_log(logging.ERROR,
                               f'--FAILED--  {email} we already have user with this Email')
            return
        elif username:
            print('Failed.  we already have user with this User name.')
            self.repo.print_to_log(logging.ERROR,
                               f'--FAILED--  {username}  we already have user with this User name.')
            return
        else:
            self.repo.add(user)
            self.repo.print_to_log(logging.INFO,
                           f'--Sucsses--  user created: {user}')


    def add_administrator(self, administrator):
        self.repo.add(administrator)