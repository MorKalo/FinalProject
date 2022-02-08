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
from LoginToken import LoginToken
from Db_config import local_session, create_all_entities
from Init_db import Init_db


repo = DbRepo(local_session)

init=Init_db()
init.reset_all_db()
create_all_entities()
init.insert_test_db()
#repo.deleteAllTasks()

airfac=AirLineFacade(LoginToken(id=1, name='test', role=1))
#airfac.get_my_flights()
#airfac.update_flight(2, {'origin_country_id':3})
#fli2=Flight( airline_Company_Id=1, origin_Country_id=2, destination_Country_id=1,
              #           departure_Time=datetime(2022, 3, 30, 15, 0, 0),
             #landing_Time=datetime(2022, 3, 30, 17, 0, 0), remaining_Tickets=-3)
#airfac.add_flight(fli2)
#airfac.remove_flight(1, 2)
#air1=AirlineCompany(id=1, {country_id=2} )
airfac=AirLineFacade(LoginToken(id=2, name='turkish', role=1))
#mork=(id=2, name='kkkkkkk')
#airli.update_airline(mork)
fli=Flight(id=2, origin_Country_id=1, destination_Country_id=1, airline_Company_Id=2)
#airfac.add_flight(fli)

adm=AdministratorFacade(LoginToken(id=3, name='peleg', role=3))
#usr=User(username='ploli', password='lol', email='li', user_role=3)
#shoki=Customer(first_name='shoki', last_name='koki',  phone_number='0502111204',
#                                   credit_card_no='1234569')
#adm.create_customer(usr, shoki)
#adm.remove_airline(2)
#adm.remove_customer(1)
#adm.remove_administrator(1)
#cus=CustomerFacade(LoginToken(id=1, name='shlomi', role=2))
#cus.add_ticket(Ticket(flight_id=2, customer_id=1))
airfac=AirLineFacade(LoginToken(id=2, name='turkish', role=1))
newflight=Flight(airline_Company_Id=2, origin_Country_id=2, destination_Country_id=1,  departure_Time=datetime(2022, 3, 30, 21, 0, 0),
                             landing_Time=datetime(2022, 3, 28, 16, 0, 0))
airfac.add_flight(newflight)