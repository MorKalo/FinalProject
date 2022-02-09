from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
import logging





connection_string = 'postgresql+psycopg2://postgres:admin@localhost/flights_test_db'
#connection_string = 'postgresql+psycopg2://postgres:admin@localhost/flights_db'


Base = declarative_base()

# create table for every class that inherits from Base
def create_all_entities():
    Base.metadata.create_all(engine)

Session = sessionmaker()
engine = create_engine(connection_string, echo=True)
local_session = Session(bind=engine)


