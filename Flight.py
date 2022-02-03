from datetime import datetime
from sqlalchemy import Column, Integer,BigInteger, String, DateTime, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship, backref
from Db_config import Base
from AirlineCompany import AirlineCompany
from Country import Country

class Flight(Base):
    __tablename__ = 'flights'

    id = Column(BigInteger(), primary_key=True, autoincrement=True)
    airline_Company_Id= Column(BigInteger, ForeignKey('airline_companies.id'))
    origin_Country_id= Column(Integer, ForeignKey ('countries.id'), nullable=False)
    destination_Country_id=Column(Integer, ForeignKey ('countries.id'), nullable=False)
    departure_Time=Column(DateTime()) #add nullable=False
    landing_Time=Column(DateTime()) #nullable=False
    remaining_Tickets=Column(Integer(), nullable=False)


    flightv = relationship('AirlineCompany',  backref=backref("flightsv", uselist=True))
    origin = relationship('Country', foreign_keys=[origin_Country_id], backref=backref("origin_flight", uselist=True))
    destination = relationship('Country', foreign_keys=[destination_Country_id], backref=backref("dest_flight", uselist=True))

    def __repr__(self):
        return f'\n<id={self.id} airline_Company_Id={self.airline_Company_Id} origin_Country_id{self.origin_Country_id}\
         destination_Country_id = {self.destination_Country_id} departure_Time={self.departure_Time}\
          landing_Time={self.landing_Time} remaining_Tickets={self.remaining_Tickets}>'

    def __str__(self):
        return f'\n<id={self.id} airline_Company_Id={self.airline_Company_Id} origin_Country_id{self.origin_Country_id}\
         destination_Country_id = {self.destination_Country_id} departure_Time={self.departure_Time}\
          landing_Time={self.landing_Time} remaining_Tickets={self.remaining_Tickets}>'


