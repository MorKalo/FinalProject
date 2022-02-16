import sys
from datetime import datetime
from DbRepo import DbRepo
from sqlalchemy import asc, text, desc
from Flight import Flight
from Country import Country
from AirlineCompany import AirlineCompany
from Customer import Customer
from User_Roles import User_Roles
from Ticket import Ticket
from User import User
from Administrator import Administrator
from AdministratorFacade import AdministratorFacade
from AirLineFacade import AirLineFacade
from CustomerFacade import CustomerFacade
from AnonymusFacade import AnonymusFacade
from datetime import *
from Db_config import local_session, create_all_entities

class Init_db():

    def __init__(self):
        self.repo=DbRepo(local_session)


    def reset_all_db(self):
        self.repo.drop_all_table()
        create_all_entities()

    def insert_test_db(self):
        # add countries
        self.repo.add(Country(name='United States'))
        self.repo.add(Country(name='Mexico'))
        # add user role
        self.repo.add(User_Roles(role_name='airline_company'))
        self.repo.add(User_Roles(role_name='customer'))
        self.repo.add(User_Roles(role_name='administrator'))
        self.repo.add(User_Roles(role_name='Anonymus'))
        # add user's
        self.repo.add(User(username='Delta_airline', password='123', email='delta@gmail.com', user_role=1))
        self.repo.add(User(username='Nanos', password='324', email='nanos2@gmail.com', user_role=2))
        self.repo.add(User(username='MorMor', password='213', email='mor.kallo@gmail.com', user_role=3))
        self.repo.add(User(username='Moti5k', password='232', email='moti@gmail.com', user_role=3))
        self.repo.add(User(username='pninosh', password='786', email='pnina@gmail.com', user_role=2))
        self.repo.add(User(username='turkish', password='97', email='turkish@gmail.com', user_role=1))
        # add admin
        self.repo.add(Administrator(first_name='Mor', last_name='Kalo', user_id=3))
        self.repo.add(Administrator(first_name='Moti', last_name='Kalo', user_id=4))
        # add customer's
        self.repo.add(Customer(first_name='Shlomi', last_name='Moshe', user_id=2, phone_number='0502111201',
                                   credit_card_no='123456'))
        self.repo.add(Customer(first_name='Pnina', last_name='Kalo', user_id=5, credit_card_no=45802601))
        # add airline's
        self.repo.add(AirlineCompany(name="Delta", country_id=1, user_id=1))
        self.repo.add(AirlineCompany(name="Turkish AirLine", country_id=2, user_id=6))
        # add flight's
        self.repo.add(Flight(airline_Company_Id=1, origin_Country_id=2, destination_Country_id=1,
                         departure_Time=datetime(2022, 3, 30, 15, 0, 0),
                         landing_Time=datetime(2022, 3, 30, 20, 0, 0), remaining_Tickets=23))
        self.repo.add(Flight(airline_Company_Id=2, origin_Country_id=1, destination_Country_id=2,
                         departure_Time=datetime(2022, 2, 10, 11, 0, 0),
                         landing_Time=datetime(2022, 2, 10, 12, 0, 0), remaining_Tickets=0))
        self.repo.add(Flight(airline_Company_Id=1, origin_Country_id=1, destination_Country_id=2,
                             departure_Time=datetime(2022, 3, 30, 16, 0, 0),
                             landing_Time=datetime(2022, 3, 30, 20, 0, 0), remaining_Tickets=65))
        # add tickets's
        self.repo.add(Ticket(flight_id=1, customer_id=1))
        self.repo.add(Ticket(flight_id=2, customer_id=2))
