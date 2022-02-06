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
  #                       departure_Time=datetime(2022, 3, 30, 15, 0, 0),
 #            landing_Time=datetime(2022, 3, 30, 13, 0, 0), remaining_Tickets=12)
#airfac.add_flight(fli2)
airfac.remove_flight(1, 2)

adm=AdministratorFacade(LoginToken(id=3, name='peleg', role=3))
#usr=User(username='ploli', password='lol', email='li', user_role=3)
#shoki=Customer(first_name='shoki', last_name='koki',  phone_number='0502111204',
#                                   credit_card_no='1234569')
#adm.create_customer(usr, shoki)
#adm.remove_airline(2)
#adm.remove_customer(1)
adm.remove_administrator(1)