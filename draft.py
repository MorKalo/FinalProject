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


def get_my_tickets(self):  # FUNC BY ID
    self.repo.print_to_log(logging.DEBUG, f'start to get my tickets func.')
    checkcustomer = self.repo.get_by_condition(Customer, lambda query: query.filter(Customer.id == customer_id).all())
    if not checkcustomer:
        print(f' Failed. We cant find this customer id')
        self.repo.print_to_log(logging.ERROR,
                               f'--FAILED-- we cant find customer id {customer_id}')
    else:
        self.repo.print_to_log(logging.INFO,
                               f'--SUCCESS--  get ticket by customer id  {customer_id} is finish Successfully')
        return self.repo.get_by_condition(Ticket, lambda query: query.filter(Ticket.customer_id == customer_id).all())


__________________________________________________--

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


def get_flights_by_airlinecompany(self, airline):
    return self.repo.get_by_condition(Flight, Flight.airline_Company_Id == airline).all()

    # i cant remove airline if there is flight for this airline id.


def remove_airline(self, airline_id):  # remove by airline id
    self.repo.print_to_log(logging.DEBUG, f'remove airline is about to happen')
    if not self.repo.get_by_condition(AirlineCompany,
                                      lambda query: query.filter(AirlineCompany.id == airline_id).all()):
        print('Failed, we cant find this airline number')
        self.repo.print_to_log(logging.ERROR,
                               f'--FAILED--    we cant find {airline_id} airline number')
    else:
        self.repo.delete(AirlineCompany, airline_id)
        self.repo.print_to_log(logging.INFO,
                               f'--Sucsses--  airline company id {airline_id} is removed')

    # i cant remove customer if there is ticket for this customer id.


def remove_customer(self, customer_id):  # remove by customer id
    self.repo.print_to_log(logging.DEBUG, f'remove customer is about to happen')
    if not self.repo.get_by_condition(Customer,
                                      lambda query: query.filter(Customer.id == customer_id).all()):
        print('Failed, we cant find this customer id number')
        self.repo.print_to_log(logging.ERROR,
                               f'--FAILED--    we cant find {customer_id} customer id')
    else:
        self.repo.delete(Customer, customer_id)
        self.repo.print_to_log(logging.INFO,
                               f'--Sucsses--  customer id {customer_id} is removed')

    # WORK GOOOD


def remove_administrator(self, administrator_id):  # remove by administrator id
    self.repo.print_to_log(logging.DEBUG, f'remove administrator is about to happen')
    if not self.repo.get_by_condition(Administrator,
                                      lambda query: query.filter(Administrator.id == administrator_id).all()):
        print('Failed, we cant find this administrator id number')
        self.repo.print_to_log(logging.ERROR,
                               f'--FAILED--    we cant find {administrator_id} administrator id')
    else:
        self.repo.delete(Administrator, administrator_id)
        self.repo.print_to_log(logging.INFO,
                               f'--Sucsses--  administrator id {administrator_id} is removed')







    def add_airline(self, user, airline):#use this func from create airline only. user and airline are object.
        self.repo.print_to_log(logging.DEBUG, f'add new airline is about to happen')
        if  self.repo.get_by_condition(AirlineCompany, lambda query: query.filter(
                    AirlineCompany.name == airline.name).all()):
            self.repo.print_to_log(logging.ERROR,
                        f'--FAILED--  {airline.name} we already have Airline company with this name')
            raise NameNeedToBeDifrentException
     #       print('Failed.  we already have Airline company with this name.')
      #      return
        if not self.repo.get_by_condition(Country,
                                          lambda query: query.filter(Country.id == airline.country_id).all()):
            print(f' Failed.  the country {airline.country_id} does not exist.')
            return
        airline.user_id=user.id
        self.repo.add(airline)
        return




    def add_customer(self, user, customer):
        self.repo.print_to_log(logging.DEBUG, f'adding customer is about to happen')
        # trying to find this customer in Customer, and to check if there isnt another customer with does deatils:
        # Phone number
        if self.repo.get_by_condition(Customer,
                                      lambda query: query.filter(
                                          Customer.phone_number == customer.phone_number).all()):
            print('Failed, a customer with this phone number is already exists.')
            self.repo.print_to_log(logging.ERROR,
                                   f'--FAILED--  {customer.id} a customer with the same Phone number {customer.phone_number}'
                                   f'is alredy exists.')
            return
        # Credit-Card number
        if self.repo.get_by_condition(Customer, lambda query: query.filter(
                                          Customer.credit_card_no == customer.credit_card_no).all()):
            print('Failed, a customer with this credit card number is already exists.')
            self.repo.print_to_log(logging.ERROR,
                                   f'--FAILED--  {customer.id} a customer with the Credit card  number {customer.credit_card_no}'
                                   f'is alredy exists.')
            return
        customer.user_id = user.id
        self.repo.add(customer)


#AirlineFacade
airli=AirLineFacade(LoginToken(id=2, name='turkish', role=1))
mork=AirlineCompany(id=2, name='kkkkkkk' )
airli.update_airline(mork)
______________________________________________________________
********Customer Facade*********

#cust=CustomerFacade(LoginToken(id=2, name='shlomi', role=2))
#cust.print_token()

#annas=AnonymusFacade()
#annas.login(username='Nanos', password='324')

cust=CustomerFacade(LoginToken(id=1, name='shlomi', role=2))
shlomi=Customer(last_name='shlomki', phone_number='0376526284')
#cust.update_customer(shlomi)
tick=Ticket(flight_id=2, customer_id=1)
#cust.add_ticket(tick)
#cust.remove_ticket(1)
cust.get_my_tickets()
____________________________-
#check DBrepo func
print(repo.getAirlinesByCountry(1))
print(repo.getFlightsByOriginCountryId(2))
print(repo.getFlightsByDestinationCountryId(4))
print(repo.getFlightsByCustomer(4))
repo.update(Customer, {'last_name':'Kalo'})


#check Administrator Facade func
facadmin=AdministratorFacade()

air1=AirlineCompany(name='Bangkok Airways', country_id=3, user_id=8)
facadmin.add_airline(air1)

cus1=Customer(first_name='ofri', last_name='moshe', user_id=9)
facadmin.add_customer(cus1)

aadmin1=Administrator(first_name='Peleg', last_name='moshe', user_id=9)
facadmin.add_administrator(aadmin1)
facadmin.remove_administrator(1)
facadmin.remove_customer(1)
facadmin.remove_airline(6)
facadmin.get_all_customers()

#check Customer Facade func
cusfac=CustomerFacade()
tick1=Ticket(flight_id=5, customer_id=2 )
cusfac.add_ticket(tick1)
#print(cusfac.get_customer(2))
cus3 = Customer(first_name='Sharon', last_name='Moshe', user_id=7)
cusfac.add_customer(cus3)
flight6 = Flight(airline_Company_Id=3, origin_Country_id=3, destination_Country_id=2, remaining_Tickets=123)
airfac.add_airline(flight6)
print ('ddddddddddddddddddddddddd')
#print(airfac.get_flights_by_parametres(3, 4))
cusfac.update_customer(1, {'last_name':'Kalo Moshe'})

#check Airline Facade func
airfac=AirLineFacade()
print(airfac.get_flights_by_airline(2))
#airfac.get_update_airline(3, AirlineCompany.country_id : 2) #NEED TO CHECK IT
#airfac.get_update_flight(3, Flight.origin_Country_id : 2) #NEED TO CHECK IT
#airfac.update_airline(2, {'name':'Turkish Airline'})
airfac.update_flight(2, {'remaining_Tickets':5})

#check Administrator Facade func
facadmin=AdministratorFacade()
facadmin.remove_administrator(1)

airfac=AirLineFacade()
airfac.update_flight(2, {'remaining_Tickets':5})


def remove_ticket(self, ticket_id):  # cant get customer id
    self.repo.print_to_log(logging.DEBUG, f'removing ticket is about to happen')
    ticket_exists = self.repo.get_by_condition(Ticket, lambda query: query.filter(Ticket.id == ticket_id).all())
    if not ticket_exists:
        self.repo.print_to_log(logging.ERROR,
                               f'--FAILED--  customer id {Ticket.customer_id} trying to remove ticket id {ticket_id}'
                               f'  but we cant find this ticket')
        raise TicketNotFoundException
    else:
        fullticket = self.repo.get_by_id(Ticket, ticket_id)
        flight = self.repo.get_by_condition(Flight, lambda query: query.filter(Flight.id == fullticket.flight_id).all())
        print(f' the flight is {flight}')
        print(flight[0].remaining_Tickets)
        flight[0].remaining_Tickets += 1
        print(flight[0].remaining_Tickets)
        # self.repo.delete_by_column_value(Ticket, Ticket.id, ticket_id)

    def update_customer(self, customer_id, data):#NEED TO DO TEST ABOUT THE data
        if not isinstance(customer_id, int):
            print('Customer ID must to be integer')
            return
        if customer_id <= 0 :
            print('Customer ID must to be positive')
            return
        if self.repo.get_by_condition(Customer,
                                      lambda query: query.filter(Customer.phone_number == customer.phone_number).all()) and \
                self.repo.get_by_condition(Customer, lambda query: query.filter(
                    Customer.phone_no == customer.phone_no).all()) != updated_customer:
            print('Function failed, a customer with this phone number is already exists.')
            return
        self.repo.update_by_column_value(Customer, 'id', customer_id, data)

        def update_by_id(self, table_class, id_column_name, id,
                         data):  # data is a dictionary of all the new columns and values
            self.local_session.query(table_class).filter(table_class.id == id_).update(data)
            self.local_session.commit()

            # adfac=AdministratorFacade()
            # uair6=User(username='loli', email='loli@gmail.com', user_role=1)
            # air6=AirlineCompany(name='loi', country_id=6)
            # adfac.add_airline(uair6, air6)

            # annas=AnonymusFacade()
            # Mor=User(username='akj', password='234', email='mor.ka@gmail.com', user_role=3)
            # Morcust=Customer(first_name='soli', last_name='holy', address='something', phone_number='0502111202',
            #                 credit_card_no='1234567')
            # airfac=AirLineFacade(LoginToken(id=2, name='Mor', role=2))
            # airfac.get_flights_by_airline(2)
            # air=AirlineCompany(id=4, name='Deltaj')
            # airfac.update_airline(air)

            # fli=Flight(id=3, origin_Country_id=3, destination_Country_id=5 )
            # airfac.update_flight(fli)
            ____________________________________

#MAIN


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
#airline1 = AirlineCompany(name='al', country_id=1)
#customer1=Customer(first_name='alijd', last_name='ddd', phone_number='0502111205',
#                                   credit_card_no='123456')
#user1 = User(username='arkia', password='arki', email='arkia@gmail.com', user_role=1)
#adm.create_customer(user1, customer1)
adm.remove_customer(2)
#usr=User(username='ploli', password='lol', email='li', user_role=3)
#shoki=Customer(first_name='shoki', last_name='koki',  phone_number='0502111204',
#                                   credit_card_no='1234569')
#adm.create_customer(usr, shoki)
#adm.remove_airline(2)
#adm.remove_customer(1)
#adm.remove_administrator(1)
#cus=CustomerFacade(LoginToken(id=1, name='shlomi', role=2))
#cus.add_ticket(Ticket(flight_id=2, customer_id=1))
#airfac=AirLineFacade(LoginToken(id=2, name='turkish', role=1))
#newflight=Flight(airline_Company_Id=2, origin_Country_id=2, destination_Country_id=1,  departure_Time=datetime(2022, 3, 30, 21, 0, 0),
#                             landing_Time=datetime(2022, 3, 28, 16, 0, 0))
#airfac.add_flight(newflight)
