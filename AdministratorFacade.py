#need to insert token. remove airline dont work.
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
from Flight import Flight


class AdministratorFacade(BaseFacade):

    def __init__(self, logintoken):
        self.repo=DbRepo(local_session)
        self.logintoken = logintoken


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
                                   f'--FAILED--   we cant create this user "{user}" and airline company "{airline}" .')


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


    def create_admin(self, user, administrator):#user and admin are object
        annfacade=AnonymusFacade()
        if annfacade.create_new_user(user):
            self.add_administrator(user, administrator)
            self.repo.print_to_log(logging.INFO,
                           f'--Sucsses--  User created: {user}, Administrator created: {administrator}')
        else:
            print (f'--Failed-- we cant create this user and Administrator')
            self.repo.print_to_log(logging.ERROR,
                                   f'--FAILED--   we cant create this user "{user}" and Administrator{administrator} .')


    def add_administrator(self, user, administrator):#use this func from create admin only.
        self.repo.print_to_log(logging.DEBUG, f'add new admin is about to happen')
        if user.user_role!=3:
            print('Failed. User role need to be "Administrator".')
            self.repo.print_to_log(logging.ERROR,
                                   f'--FAILED--   User role need to be "Administrator" but we get {user.user_role} .')
            return
        administrator.user_id=user.id
        self.repo.add(administrator)
        return


    def create_customer(self, user, customer):
        annfacade = AnonymusFacade()
        if annfacade.create_new_user(user):
            self.add_administrator(user, customer)
            self.repo.print_to_log(logging.INFO,
                                   f'--Sucsses--  User created: {user}, Administrator created: {customer}')
        else:
            print(f'--Failed-- we cant create this user and Administrator')
            self.repo.print_to_log(logging.ERROR,
                                   f'--FAILED--   we cant create this user "{user}" and Administrator{customer} .')


    def add_customer(self, user, customer):  # IF there is a error because one of the unique fields, delete the user?
#            if not self.create_new_user(user):
#                print('We unable to create  the user, please check the data and try again later ')
#                self.repo.print_to_log(logging.CRITICAL,
#                                       f'--FAILED-- We unable to create  the user "{user.username}"')
#                return
#            else:
#                self.repo.print_to_log(logging.DEBUG, f'Adding customer is about to happen')
                # trying to find this customer in Customer, and to check if there isnt another customer
                # with does deatils:
                # Phone number
                if self.repo.get_by_condition(Customer, lambda query: query.filter(
                        Customer.phone_number == customer.phone_number).all()):
                    print('Failed, a customer with this phone number is already exists.')
                    self.repo.print_to_log(logging.ERROR,
                                           f'--FAILED--  we unable to create the customer for user id  {user.id}'
                                           f' because there is a customer with the same Phone number {customer.phone_number}')
                    return
                # Credit-Card number
                elif self.repo.get_by_condition(Customer, lambda query: query.filter(
                        Customer.credit_card_no == customer.credit_card_no).all()):
                    print('Failed, a customer with this credit card number is already exists.')
                    self.repo.print_to_log(logging.ERROR,
                                           f'--FAILED--  we unable to create the customer for user id  {user.id}'
                                           f' because there is a customer with the same credit card number {customer.credit_card_no}')
                    return
                else:
                    customer.user_id = user.id  # getting the user id from the user we already create
                    self.repo.add(customer)
                    self.repo.update(User, user.id, {User.user_role: 2})
                    self.repo.print_to_log(logging.INFO,
                                           f'--Sucsses-- the customer {customer.id, customer.first_name, customer.last_name}'
                                           f'   was created successfully, his details:   address:{customer.address},'
                                           f' phone number:{customer.phone_number}, credit card number:{customer.credit_card_no}  ')
                    return


    def get_flights_by_airlinecompany(self, airline):
        return  self.repo.get_by_condition(Flight, Flight.airline_Company_Id==airline).all()

    #i cant remove airline if there is flight for this airline id.
    def remove_airline(self, airline_id):#remove by airline id
        self.repo.print_to_log(logging.DEBUG, f'remove airline is about to happen')
        if not self.repo.get_by_condition(AirlineCompany,
                                          lambda query: query.filter(AirlineCompany.id == airline_id).all()):
            print('Failed, we cant find this airline number')
            self.repo.print_to_log(logging.ERROR,
                        f'--FAILED--    we cant find {airline_id} airline number')
        else:
            self.repo.delete(AirlineCompany, airline_id)
            self.repo.print_to_log(logging.INFO,
                                   f'--Sucsses--  airline company id {airline_id} is removed')


    #i cant remove customer if there is ticket for this customer id.
    def remove_customer(self, customer_id):#remove by customer id
        self.repo.print_to_log(logging.DEBUG, f'remove customer is about to happen')
        if not self.repo.get_by_condition(Customer,
                                          lambda query: query.filter(Customer.id == customer_id).all()):
            print('Failed, we cant find this customer id number')
            self.repo.print_to_log(logging.ERROR,
                        f'--FAILED--    we cant find {customer_id} customer id')
        else:
            self.repo.delete(Customer, customer_id)
            self.repo.print_to_log(logging.INFO,
                                   f'--Sucsses--  customer id {customer_id} is removed')

 #WORK GOOOD
    def remove_administrator(self, administrator_id):#remove by administrator id
        self.repo.print_to_log(logging.DEBUG, f'remove administrator is about to happen')
        if not self.repo.get_by_condition(Administrator,
                                          lambda query: query.filter(Administrator.id == administrator_id).all()):
            print('Failed, we cant find this administrator id number')
            self.repo.print_to_log(logging.ERROR,
                        f'--FAILED--    we cant find {administrator_id} administrator id')
        else:
            self.repo.delete(Administrator, administrator_id)
            self.repo.print_to_log(logging.INFO,
                                   f'--Sucsses--  administrator id {administrator_id} is removed')

