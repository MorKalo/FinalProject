import pytest
from Init_db import *
import time
from DbRepo import DbRepo
import datetime
from Flight import *
from AirlineCompany import AirlineCompany
from AirLineFacade import AirLineFacade
from UsernotauthorizedException import UsernotauthorizedException
from TicketNotFoundException import TicketNotFoundException
from FlightNotFoundException import FlightNotFoundException
from NoMoreTicketsForFlightsException import NoMoreTicketsForFlightsException


repo=DbRepo(local_session)

@pytest.fixture(scope='session', autouse=True)
def dao_connection_test():
    anon_facade=AnonymusFacade()
    return anon_facade.login('turkish', '97')



@pytest.fixture(scope='function', autouse=True)
def dao_reset_db(dao_connection_test):
    init=Init_db()
    init.reset_all_db()
    create_all_entities()
    init.insert_test_db()
    return

@pytest.fixture(scope='function', autouse=True)
def dao_init():
    print('testing initialize')
    yield()
    print('cleanup, after')
    time.sleep(3)

#get mt ticket flight func:

def test_get_my_tickets(dao_connection_test):
    assert dao_connection_test.get_my_flights() != None

#update airline func:

def test_update_airline_UsernotauthorizedException(dao_connection_test):
    with pytest.raises(UsernotauthorizedException):
        airline=AirlineCompany(id=1)
        actual = dao_connection_test.update_airline(airline)
        assert actual == False

def test_update_airline_same_name(dao_connection_test):
    airline=AirlineCompany(id=2, name='Delta')
    actual = dao_connection_test.update_airline(airline)
    assert actual == False

#add flight func:

def test_add_flight_UsernotauthorizedException(dao_connection_test):
    with pytest.raises(UsernotauthorizedException):
        flight=Flight(airline_Company_Id=1, origin_Country_id=1, destination_Country_id=2)
        actual = dao_connection_test.add_flight(flight)
        assert actual == False

def test_add_flight_origin_country_not_exsits(dao_connection_test):
    flight=Flight(airline_Company_Id=2, origin_Country_id=3, destination_Country_id=2)
    actual = dao_connection_test.add_flight(flight)
    assert actual == False

def test_add_flight_destination_country_not_exsits(dao_connection_test):
    flight=Flight(airline_Company_Id=2, origin_Country_id=2, destination_Country_id=4)
    actual = dao_connection_test.add_flight(flight)
    assert actual == False


def test_add_flight_origin_and_destination_same(dao_connection_test):#need to finish
    flight=Flight(airline_Company_Id=2, origin_Country_id=2, destination_Country_id=2)
    actual = dao_connection_test.add_flight(flight)
    assert actual == False


def test_add_flight_landing_before_departure(dao_connection_test):#need to finish
    newflight=Flight(id=2, airline_Company_Id=2, origin_Country_id=2, destination_Country_id=1,  departure_Time=datetime(2022, 3, 30, 21, 0, 0),
                             landing_Time=datetime(2022, 3, 28, 16, 0, 0))
    actual = dao_connection_test.add_flight(newflight)
    assert actual == False


def test_update_flight_reaming_tickets_positive(dao_connection_test):
    flight=Flight(airline_Company_Id=2, origin_Country_id=2, destination_Country_id=1, remaining_Tickets=0)
    actual = dao_connection_test.add_flight(flight)
    assert actual == False


def test_update_flight_UsernotauthorizedException(dao_connection_test):
    with pytest.raises(UsernotauthorizedException):
        flight=Flight(id=2, airline_Company_Id=1, origin_Country_id=1, destination_Country_id=2)
        actual = dao_connection_test.update_flight(flight)
        assert actual == False

def test_update_flight_check_if_flight_exsits(dao_connection_test):
    with pytest.raises(UsernotauthorizedException):
        flight=Flight(id=3, airline_Company_Id=1, origin_Country_id=1, destination_Country_id=2)
        actual = dao_connection_test.update_flight(flight)
        assert actual == False

def test_update_flight_origin_country_not_exsits(dao_connection_test):
    flight=Flight(airline_Company_Id=2, origin_Country_id=3, destination_Country_id=2)
    actual = dao_connection_test.update_flight(flight)
    assert actual == False

def test_update_flight_destination_country_not_exsits(dao_connection_test):
    flight=Flight(airline_Company_Id=2, origin_Country_id=2, destination_Country_id=4)
    actual = dao_connection_test.update_flight(flight)
    assert actual == False


def test_update_flight_origin_and_destination_same(dao_connection_test):#need to finish
    flight=Flight(airline_Company_Id=2, origin_Country_id=2, destination_Country_id=2)
    actual = dao_connection_test.update_flight(flight)
    assert actual == False


def test_update_flight_landing_before_departure(dao_connection_test):#need to finish
    flight_=Flight(id=2, airline_Company_Id=2, origin_Country_id=2, destination_Country_id=1,
                   departure_Time=datetime(2022, 3, 30, 21, 0, 0),
                             landing_Time=datetime(2022, 3, 28, 16, 0, 0))
    actual = dao_connection_test.update_flight(flight_)
    assert actual == False


def test_update_flight_reaming_tickets_positive(dao_connection_test):
    flight=Flight(airline_Company_Id=2, origin_Country_id=2, destination_Country_id=1, remaining_Tickets=0)
    actual = dao_connection_test.update_flight(flight)
    assert actual == False


def test_remove_flight_check_if_flight_exsits(dao_connection_test):
        flight_id=4
        airline_id=2
        actual = dao_connection_test.remove_flight(airline_id, flight_id)
        assert actual == False

def test_remove_flight(dao_connection_test):
        airline_id = 2
        flight_id = 2
        actual = dao_connection_test.remove_flight(airline_id, flight_id)
        assert actual == True

