import pytest
from Init_db import *
import time
from DbRepo import DbRepo
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

