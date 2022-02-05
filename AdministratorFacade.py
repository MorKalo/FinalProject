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
            if not self.create_new_user(user):
                print('We unable to create  the user, please check the data and try again later ')
                self.repo.print_to_log(logging.CRITICAL,
                                       f'--FAILED-- We unable to create  the user "{user.username}"')
                return
            else:
                self.repo.print_to_log(logging.DEBUG, f'Adding customer is about to happen')

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
