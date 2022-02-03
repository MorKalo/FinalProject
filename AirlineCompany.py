from datetime import datetime
from sqlalchemy import Column, Integer,BigInteger, String, DateTime, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship, backref
from Db_config import Base
from Country import Country


class AirlineCompany(Base):
    __tablename__ = 'airline_companies'

    id = Column(BigInteger(), primary_key=True, autoincrement=True)
    name= Column(String(), unique=True)
    country_id=Column(Integer, ForeignKey ('countries.id'))
    user_id=Column(BigInteger(), ForeignKey ('users.id'),  unique=True)

    countries = relationship('Country', backref=backref("airline_country", uselist=True))
    airline_users=relationship('User',foreign_keys=[user_id], backref=backref("airline_user", uselist=True))


    def __repr__(self):
        return f'\n<id={self.id} name={self.name} country_id={self.country_id} user_id={self.user_id} >'

    def __str__(self):
        return f'\n<id={self.id} name={self.name} country_id={self.country_id} user_id={self.user_id} >'


