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

#init=Init_db()
#init.reset_all_db()
#create_all_entities()
#init.insert_test_db()
#repo.deleteAllTasks()

#cust=CustomerFacade(LoginToken(id=2, name='Mor', role=2))
#cust.print_token()

#admin=AdministratorFacade()
annas=AnonymusFacade()
annas.login(username='turkish', password='97')


#cust.get_tickets_by_customer(1)



