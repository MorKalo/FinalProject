import pytest
from Init_db import *
import time
from DbRepo import DbRepo
from LoginToken import LoginToken
from AirLineFacade import AirLineFacade
from CustomerFacade import CustomerFacade
from AdministratorFacade import AdministratorFacade
from UsernotauthorizedException import UsernotauthorizedException
from TicketNotFoundException import TicketNotFoundException
from FlightNotFoundException import FlightNotFoundException
from NoMoreTicketsForFlightsException import NoMoreTicketsForFlightsException


repo=DbRepo(local_session)

@pytest.fixture(scope='session', autouse=True)
def dao_connection_test():
    anon_facade=AnonymusFacade()
    return anon_facade.login('Nanos', '324')



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

@pytest.mark.parametrize('username, password, expected', [('turkish', '97', AirLineFacade(LoginToken(id=2, name='Turkish AirLine', role=2)))
                                                        #  ,('pninosh', '786', CustomerFacade),
                                                         # ('Moti5k', '232', AdministratorFacade),
                                                          ])
def test_login(dao_connection_test, username, password, expected):
    actual=dao_connection_test.logintoken(username, password)
    assert isinstance(actual, expected)