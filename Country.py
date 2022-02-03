from datetime import datetime
from sqlalchemy import Column, Integer,BigInteger, String, DateTime, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from Db_config import Base

class Country(Base):
    __tablename__ = 'countries'


    id = Column(Integer(), primary_key=True, autoincrement=True)
    name= Column(String(), unique=True, nullable=False)


    def __repr__(self):
        return f'\n<id={self.id} name={self.name} >'

    def __str__(self):
        return f'\n<id={self.id} name={self.name} >'


