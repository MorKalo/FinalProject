Destination_Country_id=2, Departure_Time=12:34, Landing_Time=03:45, Remaining_Tickets=12

destination = relationship('Country', backref=backref("dest_flight", uselist=True))
origin = relationship('Country', backref=backref("origin_flight", uselist=True))

dbrepo
def reset_auto_inc(self, table_class):
    self.local_session.execute(f'TRUNCATE TABLE {table_class.__tablename__} RESTART IDENTITY')



    def get_by_id(self, table_class, id):
        return self.local_session.query(table_class).get(id)

print(repo.get_by_id(User, 2))


def get_by_column_value(self, table_class, column_name, value):
    return self.local_session.query(table_class).filter(column_name == value).all()

print('> 60,000', repo.get_by_condition(Company, lambda query: query.filter(Company.salary > 60000).all()))

(name='Bangkok Airways', country_id=3, user_id=8)

######################################3



#from BaseFacade
    def get_customer(self, customer_id):
        return self.repo.get_tickets_by_customer(customer_id)

    def get_flight_by_date(self, date):
        print(self.repo.getFlightsByDepartureDate(date))

#from airline facade
    def add_airline(self, airline):
        super().add_airline(airline)

    def add_customer(self, customer):
        super().add_customer(customer)

    def add_administrator(self, administrator):
        super().add_administrator(administrator)

    def get_flights_by_parametres(self, origin_country_id, destination_country_id, landate, depdate):
        print(super().get_flight_by_parameters(origin_country_id, destination_country_id, landate, depdate))

#from customer facade:

#    def add_customer(self, customer):
#        super().add_customer(customer)






#    def add_customer(self, customer):
#        super().add_customer(customer)



#    def remove_administrator(self, administrator_id):
#        self.repo.delete(Administrator, administrator_id)

#    def remove_customer(self, customer_id):
#        self.repo.delete(Customer, customer_id)

    def remove_airline(self, airline_id):
        self.repo.delete(AirlineCompany, airline_id)

 #   def add_airline(self, airline):
#      super().add_airline(airline)'''''''''''''''''''''


def add_user(self, user):  # NEED TO DO EXCEPTION UserAlreadyExistException
    self.repo.print_to_log(logging.DEBUG, f'add new airline is about to happen')
    email = self.repo.get_by_condition(User, lambda query: query.filter(User.email == user.email).all())
    username = self.repo.get_by_condition(User, lambda query: query.filter(User.username == user.username).all())
    self.repo.print_to_log(logging.DEBUG, f'check details for user first')
    if email:
        print('Failed.  we already have user with this Email.')
        self.repo.print_to_log(logging.ERROR,
                               f'--FAILED--  {email} we already have user with this Email')
        return
    elif username:
        print('Failed.  we already have user with this User name.')
        self.repo.print_to_log(logging.ERROR,
                               f'--FAILED--  {username}  we already have user with this User name.')
        return
    else:
        self.repo.add(user)
        self.repo.print_to_log(logging.INFO,
                               f'--Sucsses--  user created: {user}')






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
admin1=Administrator(first_name='Moti', last_name='Kalo', user_id=10)
repo.add(admin1)

#add customer's
customer1=Customer(first_name='Mor', last_name='Kalo', user_id=1, phone_number='0502111201', credit_card_no='123456')
repo.add(customer1)
customer2=Customer(first_name='Shlomi', last_name='Moshe', user_id=2, credit_card_no=45802601)
repo.add(customer2)

#add airline's
airline1 = AirlineCompany(name="Delta", country_id=1, user_id=1)
repo.add(airline1)
airline2 = AirlineCompany(name="Turkish AirLine", country_id=5, user_id=4)
repo.add(airline2)
airline3 = AirlineCompany(name="JetBlue", country_id=1, user_id=7)
repo.add(airline3)
airline4 = AirlineCompany(name="El al", country_id=5, user_id=6 )
repo.add(airline4)
airline5 = AirlineCompany(name="Qatar Airways", country_id=6, user_id=5)
repo.add(airline5)

#add flight's
flight1 = Flight(airline_Company_Id=1, origin_Country_id=2, destination_Country_id=1, departure_Time=datetime(2022, 3, 30, 15, 0, 0),
                        landing_Time=datetime(2022, 3, 30, 20, 0, 0),  remaining_Tickets=12)
repo.add(flight1)
flight2 = Flight(airline_Company_Id=2, origin_Country_id=3, destination_Country_id=4, departure_Time=datetime(2022, 2, 10, 11, 0, 0),
                        landing_Time=datetime(2022, 2, 10, 12, 0, 0), remaining_Tickets=43)
repo.add(flight2)
flight3 = Flight(airline_Company_Id=3, origin_Country_id=5, destination_Country_id=2, departure_Time=datetime(2022, 2, 12, 12, 0, 0),
                        landing_Time=datetime(2022, 2, 13, 6, 0, 0), remaining_Tickets=123)
repo.add(flight3)
flight4 = Flight(airline_Company_Id=2, origin_Country_id=1, destination_Country_id=3, departure_Time=datetime(2022, 2, 16, 3, 0, 0),
                        landing_Time=datetime(2022, 2, 16, 12, 0, 0), remaining_Tickets=234)
repo.add(flight4)
flight5 = Flight(airline_Company_Id=5, origin_Country_id=4, destination_Country_id=5, departure_Time=datetime(2022, 2, 28, 23, 0, 0),
                        landing_Time=datetime(2022, 3, 1, 3, 0, 0), remaining_Tickets=0)
repo.add(flight5)

#add tickets's
ticket1=Ticket(flight_id=1, customer_id=1 )
repo.add(ticket1)
ticket2=Ticket(flight_id=2, customer_id=1 )
repo.add(ticket2)

adminf=AdministratorFacade()
airus=User(username='hololol', password='a1234', email='tokok@gmail.com', user_role=1)
airl=AirlineCompany(name='hololo', country_id=3)
#airus2=User(username='MorMor', user_role=1)
#print (f' holllllllllla  {airus.username}')
#adminu=User(username='hololol', password='a1234', email='tokok@gmail.com', user_role=3)
#admin1=Administrator(first_name='ziva', last_name='sides')
#custu=User(username='MorMor', password='a1234', email='tokok@gmail.com', user_role=3)
#cust1=Customer(first_name='shiri', last_name='gol', phone_number='1234567', credit_card_no='324234')
#airf.create_customer(custu, cust1)
adminf.remove_administrator(1)
