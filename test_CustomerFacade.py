import pytest
from CustomerFacade import CustomerFacade
from Init_db import *

@pytest.fixture(scope='session', autouse=True)
def dao_connection_test():
    print('initialize before each function')
    return CustomerFacade()


@pytest.fixture(scope='function', autouse=True)
def dao_reset_db(dao_connection_test):
    init=Init_db()
    init.reset_all_db()
    return

@pytest.fixture(scope='session', autouse=True)
def dao_init():
    print('testing initialize')
    yield()
    print('cleanup, after')
    time.sleep(3)

@pytest.mark.parametrize('id_, expected', [(3, None),
                                           (1, [Ticket(id=1, flight_id=1, customer_id=1)])])
def test_customer_facade_get_tickets_by_customer(dao_connection_test, id_, expected):
    actual = dao_connection_test.get_tickets_by_customer(id_)
    assert actual == expected