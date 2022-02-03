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
from User import  User
from Administrator import Administrator
from AdministratorFacade import AdministratorFacade
from AirLineFacade import AirLineFacade
from CustomerFacade import CustomerFacade
from AnonymusFacade import AnonymusFacade

from Db_config import local_session, create_all_entities


repo = DbRepo(local_session)

repo.deleteAllTasks()


create_all_entities()

#Re-establishing a database

#add countries
country1 = Country(name='United States')
repo.add(country1)
country2 = Country(name='Mexico')
repo.add(country2)
country3 = Country(name='France')
repo.add(country3)
country4 = Country(name='Japan')
repo.add(country4)
country5 = Country(name='Turkish')
repo.add(country5)
country6 = Country(name='Qatar')
repo.add(country6)

#add user role
user_role1 = User_Roles(role_name='airline_company')
repo.add(user_role1)
user_role2 = User_Roles(role_name='customer')
repo.add(user_role2)
user_role3 = User_Roles(role_name='administrator')
repo.add(user_role3)


#add user's
user1 = User(username='MorMor', password='123', email='mor.k@gmail.com', user_role=2)
repo.add(user1)
user2 = User(username='Nanos', password='324', email='nanos2@gmail.com', user_role=2)
repo.add(user2)
user3 = User(username='Delta_airline', password='213', email='delta@gmail.com', user_role=1)
repo.add(user3)
user4 = User(username='Turkish', password='123', email='turkish@walla.com', user_role=1)
repo.add(user4)
user5 = User(username='Qatar', password='123', email='Qatar@hotmail.com', user_role=1)
repo.add(user5)
user6 = User(username='El al', password='123', email='Elal@walla.com', user_role=1)
repo.add(user6)
user7 = User(username='JetBlue', password='123', email='JetBlue@gmail.com', user_role=1)
repo.add(user7)
user8 = User(username='bangkok', password='456', email='bangkok@gmail.com', user_role=1)
repo.add(user8)
user9 = User(username='ofriki', password='23', email='ofriki@gmail.com', user_role=2)
repo.add(user9)
user10 = User(username='Moti', password='1243', email='Moti@gmail.com', user_role=3)
repo.add(user10)

#add admin
admin1=Administrator(first_name='Pnina', last_name='Kalo', user_id=8)
repo.add(admin1)

#add customer's
customer1=Customer(first_name='Mor', last_name='Kalo', user_id=1, phone_number=502111201)
repo.add(customer1)
customer2=Customer(first_name='Shlomi', last_name='Moshe', user_id=2)
repo.add(customer2)

#add airline's
airline1 = AirlineCompany(name="Delta", country_id=1, user_id=1)
repo.add(airline1)
airline2 = AirlineCompany(name="Turkish AirLine", country_id=5, user_id=2)
repo.add(airline2)
airline3 = AirlineCompany(name="JetBlue", country_id=1, user_id=7)
repo.add(airline3)
airline4 = AirlineCompany(name="El al", country_id=5, user_id=6 )
repo.add(airline4)
airline5 = AirlineCompany(name="Qatar Airways", country_id=6, user_id=5)
repo.add(airline5)

#add flight's
flight1 = Flight(airline_Company_Id=1, origin_Country_id=2, destination_Country_id=1, remaining_Tickets=12)
repo.add(flight1)
flight2 = Flight(airline_Company_Id=2, origin_Country_id=3, destination_Country_id=4, remaining_Tickets=43)
repo.add(flight2)
flight3 = Flight(airline_Company_Id=3, origin_Country_id=5, destination_Country_id=2, remaining_Tickets=123)
repo.add(flight3)
flight4 = Flight(airline_Company_Id=2, origin_Country_id=1, destination_Country_id=3, remaining_Tickets=234)
repo.add(flight4)
flight5 = Flight(airline_Company_Id=5, origin_Country_id=4, destination_Country_id=5, remaining_Tickets=0)
repo.add(flight5)

#add tickets's
ticket1=Ticket(flight_id=1, customer_id=1 )
repo.add(ticket1)
ticket2=Ticket(flight_id=2, customer_id=1 )
repo.add(ticket2)