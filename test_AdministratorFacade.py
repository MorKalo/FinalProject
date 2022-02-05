import pytest
from Administrator import Administrator
from AdministratorFacade import AnonymusFacade

@pytest.fixture(scope='session', autouse=True)
def dao_init():
    print('testing initialize')
    yield()
    print('cleanup, after')
    time.sleep(3)

@pytest.fixture(scope='session')
def dao_connection_singleton():
    print('setting up SAME dao for all tests')
    return Dao()

def test_get_first(dao_connection_singleton):
    assert dao_connection.get_first() == 1

def test_get_all(dao_connection_singleton):
    assert dao_connection.get_all() == [1, 2, 3, 4, 5]