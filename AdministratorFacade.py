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
from Flight import Flight
from UsernotauthorizedException import UsernotauthorizedException



class AdministratorFacade(BaseFacade):

    def __init__(self, logintoken):
        self.repo=DbRepo(local_session)
        self.logintoken = logintoken


    def get_all_customers(self):
        self.repo.print_to_log(logging.DEBUG, f'get all customer"s is about to happen')
        return self.repo.get_all(Customer)


    def create_airline(self, user, airline):#user and airline are object
        if not self.logintoken.role == 3:
            raise UsernotauthorizedException
            return
        else:
            if super().create_new_user(user):
                self.add_airline(user, airline)
                self.repo.print_to_log(logging.INFO,
                               f'--Sucsses--  User created: {user}, Airline created: {airline}')
            else:
                print (f'--Failed-- we cant create this user and airline company')
                self.repo.print_to_log(logging.ERROR,
                                       f'--FAILED--   we cant create this user "{user}" and airline company "{airline}" .')


    def add_airline(self, user, airline):#use this func from create airline only. user and airline are object.
        # token checked at create airline func
        self.repo.print_to_log(logging.DEBUG, f'add new airline is about to happen')
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


    def create_admin(self, user, administrator):#user and admin are object
        if not self.logintoken.role == 3:
            raise UsernotauthorizedException
            return
        else:
            if super().create_new_user(user):
                self.add_administrator(user, administrator)
                self.repo.print_to_log(logging.INFO,
                               f'--Sucsses--  User created: {user}, Administrator created: {administrator}')
            else:
                print (f'--Failed-- we cant create this user and Administrator')
                self.repo.print_to_log(logging.ERROR,
                                       f'--FAILED--   we cant create this user "{user}" and Administrator{administrator} .')


    def add_administrator(self, user, administrator):#use this func from create airline only. user and admin are object.
        # token checked at create airline func
        self.repo.print_to_log(logging.DEBUG, f'add new admin is about to happen')
        administrator.user_id=user.id
        self.repo.add(administrator)
        return


    def create_customer(self, user, customer):#user and customer are object
        if not self.logintoken.role == 3:
            raise UsernotauthorizedException
            return
        else:
            if super().create_new_user(user):
                self.add_customer(user, customer)
                self.repo.print_to_log(logging.INFO,
                                       f'--Sucsses--  User created: {user}, Administrator created: {customer}')
            else:
                print(f'--Failed-- we cant create this user and Administrator')
                self.repo.print_to_log(logging.ERROR,
                                       f'--FAILED--   we cant create this user "{user}" and Administrator{customer} .')


    def add_customer(self, user, customer):
        self.repo.print_to_log(logging.DEBUG, f'adding customer is about to happen')
        # trying to find this customer in Customer, and to check if there isnt another customer with does deatils:
        # Phone number
        if self.repo.get_by_condition(Customer,
                                      lambda query: query.filter(
                                          Customer.phone_number == customer.phone_number).all()):
            print('Failed, a customer with this phone number is already exists.')
            self.repo.print_to_log(logging.ERROR,
                                   f'--FAILED--  {customer.id} a customer with the same Phone number {customer.phone_number}'
                                   f'is alredy exists.')
            return
        # Credit-Card number
        if self.repo.get_by_condition(Customer, lambda query: query.filter(
                                          Customer.credit_card_no == customer.credit_card_no).all()):
            print('Failed, a customer with this credit card number is already exists.')
            self.repo.print_to_log(logging.ERROR,
                                   f'--FAILED--  {customer.id} a customer with the Credit card  number {customer.credit_card_no}'
                                   f'is alredy exists.')
            return
        customer.user_id = user.id
        self.repo.add(customer)


    def remove_airline(self, airline_id):
        self.repo.print_to_log(logging.DEBUG, f'remove airline is about to happen')
        if not self.repo.get_by_condition(AirlineCompany,
                                              lambda query: query.filter(AirlineCompany.id == airline_id).all()):
            print(f'Failed, we cant find  this airline company id {airline_id}')
            self.repo.print_to_log(logging.ERROR,
                                   f'--FAILED--    we cant find  this airline company id {airline_id}')
        elif self.logintoken.role != 3:
                raise UsernotauthorizedException
                return
        self.repo.delete(AirlineCompany, airline_id)
        self.repo.print_to_log(logging.INFO,
                                   f'--Sucsses--  airline company id {airline_id} is removed')

    def remove_customer(self, customer_id):
        self.repo.print_to_log(logging.DEBUG, f'remove customer is about to happen')
        if not self.repo.get_by_condition(Customer,
                                              lambda query: query.filter(Customer.id == customer_id).all()):
            print(f'Failed, we cant find  this Customer  id {customer_id}')
            self.repo.print_to_log(logging.ERROR,
                                   f'--FAILED--    we cant find  this customer id {customer_id}')
        elif self.logintoken.role != 3:
                raise UsernotauthorizedException
                return
        self.repo.delete(Customer, customer_id)
        self.repo.print_to_log(logging.INFO,
                                   f'--Sucsses--  customer id {customer_id} is removed')


    def remove_administrator(self, admin_id):
        self.repo.print_to_log(logging.DEBUG, f'remove admin is about to happen')
        if not self.repo.get_by_condition(Administrator,
                                              lambda query: query.filter(Administrator.id == admin_id).all()):
            print(f'Failed, we cant find  this admin  id {admin_id}')
            self.repo.print_to_log(logging.ERROR,
                                   f'--FAILED--    we cant find  this admin id {admin_id}')
        elif self.logintoken.role != 3:
                raise UsernotauthorizedException
                return
        self.repo.delete(Administrator, admin_id)
        self.repo.print_to_log(logging.INFO,
                                   f'--Sucsses--  admin id {admin_id} is removed')
