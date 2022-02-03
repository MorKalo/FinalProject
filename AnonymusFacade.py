#NEED TO FINISH: def login, def_create new user-RESOLVE
import logging
from BaseFacade import BaseFacade
from Db_config import local_session, create_all_entities
from DbRepo import DbRepo
from Administrator import Administrator
from Flight import Flight
from Customer import Customer
from UserAlreadyExistException import *
from User import User
from AirLineFacade import AirLineFacade
from CustomerFacade import CustomerFacade
from AdministratorFacade import AdministratorFacade


class AnonymusFacade(BaseFacade):

    def __init__(self):
        self.repo=DbRepo(local_session)

    def login(self, username, password):
        user = self.repo.get_by_condition(User, lambda query: query.filter(User.username == username, User.password == password).all())

        print(user)
        if not user:
            print('Faild, we didnt find that user.')
            self.repo.print_to_log(logging.ERROR,
                                   f'--FAILED--  we didnt find that user "{username}"')
            return
        else:
            if user[0].user_role == 1:
                return AirLineFacade()
            elif user[0].user_role == 2:
                return CustomerFacade()
            elif user[0].user_role == 3:
                return AdministratorFacade()

    def create_new_user(self, user):
        #NEED TO ENTERED THE USER ID TO CUSTOMER;
        # NEED TO DO EXCEPTION UserAlreadyExistException
        print(user)
        if self.user[1] == User.username:
            raise UserAlreadyExistException()
        else:
            self.repo.add(user)
        #    super().add_customer(customer)



    def add_customer(self, customer):
        super().add_customer(customer)



