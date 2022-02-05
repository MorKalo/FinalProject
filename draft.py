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



