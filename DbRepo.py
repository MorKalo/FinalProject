import sys
from sqlalchemy import asc, text, desc, delete, update
from Db_config import local_session
from AirlineCompany import AirlineCompany
from Flight import Flight
from Ticket import Ticket
import datetime
import logging
import datetime as dt

logging.basicConfig(level='DEBUG')
logger = logging.getLogger("--DbRepo--")

logging.info('info message')

file_handler = logging.FileHandler("logfile.log")
file_handler.setLevel(logging.DEBUG)
logger.addHandler(file_handler)

class DbRepo:

    def __init__(self, local_session):
        self.local_session = local_session

    def print_to_log(self, level, msg):
        logger.log(level, f'{datetime.datetime.now()} {logging.getLevelName(level)} {msg}')

    def get_by_id(self, table_class, id):
        return self.local_session.query(table_class).get(id)


    def get_all(self, table_class):
        return self.local_session.query(table_class).all()


    def add(self, one_row):
        self.local_session.add(one_row)
        self.local_session.commit()


    def add_all(self, rows_list):
        self.local_session.add_all(rows_list)
        self.local_session.commit()

    def update(self, table_class, id, data):
        local_session.query(table_class).filter(table_class.id == id)\
            .update(data)
        self.local_session.commit()

    def update_by_id(self, table_class, id, data):  # data is a dictionary of all the new columns and values
        self.local_session.query(table_class).filter(table_class.id == id).update(data)
        self.local_session.commit()

    def update_by_column_value(self, table_class, column_name, value, data):
        #return self.local_session.query(table_class).filter(column_name == value)\
        #    .update(data)
        self.local_session.query(table_class).filter(getattr(table_class, column_name)== value).update(data)
        self.local_session.commit()

    def delete(self, table_class, id):
        local_session.query(table_class).filter(table_class.id==id).delete(synchronize_session=False)
        self.local_session.commit()


    def delete_by_column_value(self, table_class, column_name, value):
        self.local_session.query(table_class).filter(column_name == value).delete()
        self.local_session.commit()


    def getAirlinesByCountry(self, country_id):
        return self.local_session.query(AirlineCompany).get(country_id)


    def getFlightsByOriginCountryId(self, country_id):
        return self.local_session.query(Flight).filter(Flight.origin_Country_id==country_id).all()


    def getFlightsByDestinationCountryId(self, country_id):
        return self.local_session.query(Flight).filter(Flight.destination_Country_id==country_id).all()


    def getFlightsByDepartureDate(self, date):
        return self.local_session.query(Flight).filter(Flight.departure_Time == date).all()

    def getFlightsByLandingDate(self, date):
        return self.local_session.query(Flight).filter(Flight.landing_Time == date).all()


    def getFlightsByCustomer(self, customer):
        return self.local_session.query(Flight).filter(Ticket.customer_id == customer).all()

    def getFlightsByAirlineId(self, airline):
        return self.local_session.query(Flight).filter(Flight.airline_Company_Id == airline).all()

    def get_by_condition(self, table_class, cond):
        #return self.local_session.query(table_class).filter(cond).all()
        query_result = self.local_session.query(table_class)
        result = cond(query_result)
        return result


    def deleteAllTasks(self):
        self.local_session.execute(f'DROP TABLE {"countries"} cascade')
        self.local_session.execute(f'DROP TABLE {"flights"} cascade')
        self.local_session.execute(f'DROP TABLE {"airline_companies"} cascade')
        self.local_session.execute(f'DROP TABLE {"tickets"} cascade')
        self.local_session.execute(f'DROP TABLE {"users"} cascade')
        self.local_session.execute(f'DROP TABLE {"user_roles"} cascade')
        self.local_session.execute(f'DROP TABLE {"administrators"} cascade')
        self.local_session.execute(f'DROP TABLE {"customers"} cascade')
        local_session.commit();

