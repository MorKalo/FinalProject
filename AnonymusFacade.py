#there is a Q
import logging
from BaseFacade import BaseFacade
from Db_config import local_session, create_all_entities
from DbRepo import DbRepo
from Administrator import Administrator
from Flight import Flight
from Customer import Customer
from UserAlreadyExistException import *
from User import User
from AirlineCompany import AirlineCompany
from LoginToken import LoginToken


class AnonymusFacade(BaseFacade):


    def __init__(self):
        self.repo=DbRepo(local_session)

    def login(self, username, password):
        user = self.repo.get_by_condition(User, lambda query: query.filter(User.username == username).all())
        if not user:
            print('Faild, we didnt find that user.')
            self.repo.print_to_log(logging.ERROR,
                                   f'--FAILED--  we didnt find that user "{username}"')
            return
        else:
            passw= self.repo.get_by_condition(User, lambda query: query.filter(User.password == password).all())
            if not passw:
                print('Faild, wrong password.')
                self.repo.print_to_log(logging.ERROR,
                                       f'--FAILED--   wrong password for user "{username}"')
                return
            else:
                self.repo.print_to_log(logging.INFO,
                                   f'--Sucsses-- the password is match for user "{username}"')
                if user[0].user_role == 1:
                    self.repo.print_to_log(logging.INFO,
                                           f'--Sucsses-- the user "{username}" transferred to Airline Facade  ')
                    airname=self.repo.get_by_condition(AirlineCompany, lambda query: query.filter(AirlineCompany.user_id == user[0].id).all())
                    return AirLineFacade(LoginToken(user[0].id, airname[0].name, user[0].user_role))
                elif user[0].user_role == 2:
                    self.repo.print_to_log(logging.INFO,
                                           f'--Sucsses-- the user "{username}" transferred to Customer Facade  ')
                    custname=self.repo.get_by_condition(Customer, lambda query: query.filter(Customer.user_id == user[0].id).all())
                    return CustomerFacade(LoginToken(user[0].id, custname[0].first_name, user[0].user_role))
                elif user[0].user_role == 3:
                    self.repo.print_to_log(logging.INFO,
                                           f'--Sucsses-- the user "{username}" transferred to Admin Facade  ')
                    name= self.repo.get_by_condition(Administrator, lambda query: query.filter(Administrator.user_id == user[0].id).all())
                    return AdministratorFacade(
                        LoginToken(user[0].id, name[0].first_name, user[0].user_role))


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


    def add_customer(self, user, customer):#IF there is a error because one of the unique fields, delete the user?
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
            if self.repo.get_by_condition(Customer,lambda query: query.filter(
                                              Customer.phone_number == customer.phone_number).all()):
                print('Failed, a customer with this phone number is already exists.')
                self.repo.print_to_log(logging.ERROR,
                                       f'--FAILED--  we unable to create the customer for user id  {user.id}'
                                       f' because there is a customer with the same Phone number {customer.phone_number}')
                return
            # Credit-Card number
            elif self.repo.get_by_condition(Customer,lambda query: query.filter(
                                              Customer.credit_card_no == customer.credit_card_no).all()):
                print('Failed, a customer with this credit card number is already exists.')
                self.repo.print_to_log(logging.ERROR,
                                       f'--FAILED--  we unable to create the customer for user id  {user.id}'
                                       f' because there is a customer with the same credit card number {customer.credit_card_no}')
                return
            else:
                customer.user_id=user.id  #getting the user id from the user we already create
                self.repo.add(customer)
                self.repo.update(User, user.id, {User.user_role:2})
                self.repo.print_to_log(logging.INFO,
                                       f'--Sucsses-- the customer {customer.id, customer.first_name, customer.last_name}'
                                       f'   was created successfully, his details:   address:{customer.address},'
                                       f' phone number:{customer.phone_number}, credit card number:{customer.credit_card_no}  ')
                return
