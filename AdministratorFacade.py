import logging
from BaseFacade import BaseFacade
from Db_config import local_session, create_all_entities
from DbRepo import DbRepo
from Administrator import Administrator
from Customer import Customer
from AirlineCompany import AirlineCompany
from CreateUserAndObjectFailedException import CreateUserAndObjectFailedException
from User import User
from Country import Country
from LoginToken import LoginToken
from Flight import Flight
from UsernotauthorizedException import UsernotauthorizedException
from NameNeedToBeDifrentException import NameNeedToBeDifrentException
from DataExistException import DataExistException
from Logger import Logger



class AdministratorFacade(BaseFacade):

    def __init__(self, logintoken):
        super().__init__(logintoken)
        # self.logintoken = logintoken
        #self.repo=DbRepo(local_session)
        #self.logintoken = logintoken
        #self.logger = Logger.get_instance()


    def get_all_customers(self):
        self.logger.logger.debug(f'get all customer"s is about to happen for {self.logintoken}')
        return self.repo.get_all(Customer)


    def create_airline(self, user, airline):#user and airline are object
        if not self.logintoken.role == 3:
            self.logger.logger.ERROR(f'--FAILED--  user {self.logintoken.__dict__} cant create airline.')
            raise UsernotauthorizedException
        else:
            if super().create_new_user(user):
                self.logger.logger.DEBUG(f'add new airline is about to happen by {self.logintoken.__dict__}')
                if self.repo.get_by_condition(AirlineCompany, lambda query: query.filter(
                        AirlineCompany.name == airline.name).all()):
                    self.logger.logger.ERROR(f'--FAILED--  {self.logintoken.__dict__} we already have '
                                             f'Airline company with this name {airline.name}')
                    print('Failed.  we already have Airline company with this name.')
                    raise NameNeedToBeDifrentException
                if not self.repo.get_by_condition(Country,
                                                  lambda query: query.filter(Country.id == airline.country_id).all()):
                    print(f' Failed.  the country {airline.country_id} does not exist.')
                    self.logger.logger.ERROR(f'--FAILED--  {self.logintoken.__dict__}the country '
                                             f'{airline.country_id} does not exist')
                    return
                airline.user_id = user.id
                self.repo.add(airline)
                self.logger.logger.INFO(f'--Sucsses-- {self.logintoken.__dict__}  User created: {user}'
                                        f', Airline created: {airline}')
                return True
            else:
                self.logger.logger.ERROR(f'--FAILED-- {self.logintoken.__dict__}  we cant create this user'
                                         f' "{user}" and airline company "{airline}" .')
                raise CreateUserAndObjectFailedException


    def create_customer(self, user, customer):#user and customer are object
        if not self.logintoken.role == 3:
            raise UsernotauthorizedException
        else:
            if super().create_new_user(user):
                self.logger.logger.DEBUG(f' {self.logintoken.__dict__}adding customer is about to happen')
                # trying to find this customer in Customer, and to check if there isnt another customer with does deatils:
                # Phone number
                if self.repo.get_by_condition(Customer,
                                              lambda query: query.filter(
                                                  Customer.phone_number == customer.phone_number).all()):
                    print('Failed, a customer with this phone number is already exists.')
                    self.logger.logger.ERROR(f'--FAILED-- {self.logintoken.__dict__} a customer with the same'
                                             f' Phone number {customer.phone_number} is alredy exists.')
                    raise DataExistException
                # Credit-Card number
                if self.repo.get_by_condition(Customer, lambda query: query.filter(
                        Customer.credit_card_no == customer.credit_card_no).all()):
                    print('Failed, a customer with this credit card number is already exists.')
                    self.logger.logger.ERROR(f'--FAILED--  {self.logintoken.__dict__} a customer with the '
                                             f'Credit card  number {customer.credit_card_no} is alredy exists.')
                    raise DataExistException
                customer.user_id = user.id
                self.repo.add(customer)
                self.logger.logger.INFO(f'--Sucsses-- {self.logintoken.__dict__}  '
                                        f'User created: {user}, Administrator created: {customer}')
                return True
            else:
                print(f'--Failed-- we cant create this user and Administrator')
                self.logger.logger.ERROR(f'--FAILED-- {self.logintoken.__dict__}  we cant create '
                                         f'this user "{user}" and Administrator{customer} .')
                raise CreateUserAndObjectFailedException


    def create_admin(self, user, administrator):#user and admin are object
        if not self.logintoken.role == 3:
            raise UsernotauthorizedException
        else:
            if super().create_new_user(user):
                self.logger.logger.DEBUG( f' {self.logintoken.__dict__} add new admin is about to happen')
                administrator.user_id = user.id
                self.repo.add(administrator)
                self.logger.logger.INFO(f'--Sucsses-- {self.logintoken.__dict__} User created: {user}, '
                                        f'Administrator created: {administrator}')
                return True
            else:
                print (f'--Failed-- we cant create this user and Administrator')
                self.logger.logger.ERROR(f'--FAILED-- {self.logintoken.__dict__}  we cant create this'
                                         f' user "{user}" and Administrator{administrator} .')
                raise CreateUserAndObjectFailedException


    def remove_airline(self, airline_id):
        self.logger.logger.DEBUG( f'{self.logintoken.__dict__} remove airline is about to happen')
        if not self.repo.get_by_condition(AirlineCompany,
                                              lambda query: query.filter(AirlineCompany.id == airline_id).all()):
            print(f'Failed, we cant find  this airline company id {airline_id}')
            self.logger.logger.ERROR(f'--FAILED--  {self.logintoken.__dict__}  we cant find  this airline'
                                     f' company id {airline_id}')
            return False
        elif self.logintoken.role != 3:
                raise UsernotauthorizedException
        self.repo.delete(AirlineCompany, airline_id)
        self.repo.print_to_log(logging.INFO,
                                   f'--Sucsses--  airline company id {airline_id} is removed')
        self.logger.logger.INFO(f'--Sucsses--  {self.logintoken.__dict__}  airline company id {airline_id} is removed')
        return True

    def remove_customer(self, customer_id):
        self.logger.logger.DEBUG( f' {self.logintoken.__dict__}  remove customer is about to happen')
        if not self.repo.get_by_condition(Customer,
                                              lambda query: query.filter(Customer.id == customer_id).all()):
            print(f'Failed, we cant find  this Customer  id {customer_id}')
            self.logger.logger.DEBUG.ERROR(f'--FAILED--  {self.logintoken.__dict__}  we cant find  this customer'
                                           f' id {customer_id}')
            return False
        elif self.logintoken.role != 3:
                raise UsernotauthorizedException
        self.repo.delete(Customer, customer_id)
        self.repo.logger.logger.INFO(f'--Sucsses-- {self.logintoken.__dict__} customer id {customer_id} is removed')
        return True

    def remove_administrator(self, admin_id):
        self.logger.logger.DEBUG( f' {self.logintoken.__dict__} remove admin is about to happen')
        if not self.repo.get_by_condition(Administrator,
                                              lambda query: query.filter(Administrator.id == admin_id).all()):
            print(f'Failed, we cant find  this admin  id {admin_id}')
            self.logger.logger.ERROR(f'--FAILED--  {self.logintoken.__dict__}  we cant find  this admin id {admin_id}')
            return False
        elif self.logintoken.role != 3:
                raise UsernotauthorizedException
        self.repo.delete(Administrator, admin_id)
        self.logger.logger.INFO(f'--Sucsses-- {self.logintoken.__dict__} admin id {admin_id} is removed')
        return True