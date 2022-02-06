import pytest
from CustomerFacade import CustomerFacade
from Init_db import *
import time
from DbRepo import DbRepo
from LoginToken import LoginToken
from UsernotauthorizedException import UsernotauthorizedException

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


def test_get_my_tickets(dao_connection_test):
    assert dao_connection_test.get_my_tickets() != None


def test_remove_tickets(dao_connection_test ):
    ticket_id=1
    actual=dao_connection_test.remove_ticket(ticket_id)
    assert actual==True

def test_remove_tickets_exception(dao_connection_test):
    with pytest.raises(UsernotauthorizedException):
        ticket_id = 2
        actual = dao_connection_test.remove_ticket(ticket_id)
        assert actual == False

    #ticket_id=1
    #dao_connection_test.remove_ticket(ticket_id)
    #ticketafter=dao_connection_test.get_my_tickets()
    #assert Ticket.id==1 not in 'tickets'

#@pytest.mark.parametrize('ticket, expected', [
#                                              (Ticket(flight_id=1, customer_id=1), True),
#                                             ])
#def test_add_ticket(dao_connection_test, ticket, expected):
#    actual = dao_connection_test.add_ticket(ticket)
#    assert actual == expected
