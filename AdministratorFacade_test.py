import pytest
from Init_db import *
import time
from DbRepo import DbRepo
from User import *
from Customer import *
from AirlineCompany import *
from UsernotauthorizedException import UsernotauthorizedException
from TicketNotFoundException import TicketNotFoundException
from FlightNotFoundException import FlightNotFoundException
from NoMoreTicketsForFlightsException import NoMoreTicketsForFlightsException
from NameNeedToBeDifrentException import NameNeedToBeDifrentException
from DataExistException import DataExistException

repo=DbRepo(local_session)

@pytest.fixture(scope='session', autouse=True)
def dao_connection_test():
    anon_facade=AnonymusFacade()
    return anon_facade.login('Moti5k', '232')


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

#get all customer
def test_get_my_tickets(dao_connection_test):
    assert dao_connection_test.get_all_customers() != None


#create AIRLINE
def test_create_airline(dao_connection_test):
    airline1=AirlineCompany(name='arkia', country_id=1)
    user1=User(username='arkia', password='arki', email='arkia@gmail.com', user_role=1)
    actual=dao_connection_test.create_airline(user1, airline1)
    assert actual==True

def test_create_airline_NameNeedToBeDifrentException(dao_connection_test):
    with pytest.raises(NameNeedToBeDifrentException):
        user1=User(username='tu', password='kish', email='turkishhhhhh@gmail.com', user_role=1)
        airline1=AirlineCompany(name='Delta', country_id=1)
        actual=dao_connection_test.create_airline(user1,airline1)
        assert actual==False


#create CUSTOMER
def test_create_customer(dao_connection_test):
    customer1=Customer(first_name='efi', last_name='yoni', phone_number='1234343',
                                   credit_card_no='4580260111110973')
    user1=User(username='efi', password='123', email='efi@gmail.com', user_role=2)
    actual=dao_connection_test.create_customer(user1, customer1)
    assert actual==True

def test_create_customer_with_same_phone_number(dao_connection_test):
    with pytest.raises(DataExistException):
        customer1 = Customer(first_name='efi', last_name='yoni', phone_number='0502111201',
                                 credit_card_no='4580260111110973')
        user1 = User(username='efi', password='123', email='efi@gmail.com', user_role=2)
        actual = dao_connection_test.create_customer(user1, customer1)
        assert actual == False


def test_create_customer_with_same_credit_card(dao_connection_test):
    with pytest.raises(DataExistException):
        customer1 = Customer(first_name='efi', last_name='yoni', phone_number='0502111202',
                                 credit_card_no='45802601')
        user1 = User(username='efi', password='123', email='efi@gmail.com', user_role=2)
        actual = dao_connection_test.create_customer(user1, customer1)
        assert actual == False


#Create ADMIN
def test_create_admin(dao_connection_test):
    admin1=Customer(first_name='efi', last_name='yoni')
    user1=User(username='efi', password='123', email='efi@gmail.com', user_role=3)
    actual=dao_connection_test.create_admin(user1, admin1)
    assert actual==True


#Remove_Airline
@pytest.mark.parametrize('airline_id, expected', [(4, False),
                                                (2, True)])
def test_remove_airline(dao_connection_test, airline_id, expected):
    actual=dao_connection_test.remove_airline(airline_id)
    assert actual==expected


#Remove_Customer
@pytest.mark.parametrize('customer_id, expected', [(4, False),
                                                (2, True)])
def test_remove_customer(dao_connection_test, customer_id, expected):
    actual=dao_connection_test.remove_airline(customer_id)
    assert actual==expected


#Remove_Admin
@pytest.mark.parametrize('admin_id, expected', [(4, False),
                                                (2, True)])
def test_remove_admin(dao_connection_test, admin_id, expected):
    actual=dao_connection_test.remove_airline(admin_id)
    assert actual==expected




