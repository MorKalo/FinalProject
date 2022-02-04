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