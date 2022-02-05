import pytest
from CustomerFacade import CustomerFacade
from Init_db import *
import time

@pytest.fixture(scope='session', autouse=True)
def dao_connection_test():
    print('initialize before each function')
    return CustomerFacade()


@pytest.fixture(scope='function', autouse=True)
def dao_reset_db(dao_connection_test):
    init=Init_db()
    init.reset_all_db()
    create_all_entities()
    init.insert_test_db()
    return

@pytest.fixture(scope='session', autouse=True)
def dao_init():
    print('testing initialize')
    yield()
    print('cleanup, after')
    time.sleep(3)

@pytest.mark.parametrize('id, expected', [(5, None),
                                          (1, [Ticket(id=1, flight_id=1, customer_id=1)])])
def test_get_tickets_by_customer(dao_connection_test, id, expected):
    actual = dao_connection_test.get_tickets_by_customer(id)
    assert actual == expected


@pytest.mark.parametrize('ticket_id, expected', [(5, None),
                                          (1, [Ticket(id=1, flight_id=1, customer_id=1)])])
def test_remove_tickets(dao_connection_test, ticket_id, expected):

