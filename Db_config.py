from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from Logger import Logger
import logging

config = ConfigParser()
config.read("config.conf")
connection_string = config["db"]["conn_string"]

logger = Logger.get_instance()



connection_string = 'postgresql+psycopg2://postgres:admin@localhost/flights_test_db'
#connection_string = 'postgresql+psycopg2://postgres:admin@localhost/flights_db'


Base = declarative_base()

# create table for every class that inherits from Base
def create_all_entities():
    Base.metadata.create_all(engine)

Session = sessionmaker()
engine = create_engine(connection_string, echo=True)
local_session = Session(bind=engine)


