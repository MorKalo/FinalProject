from datetime import datetime
from sqlalchemy import Column, Integer,BigInteger, String, DateTime, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from Db_config import Base

class User_Roles(Base):
    __tablename__ = 'user_roles'

    id = Column(Integer(), primary_key=True, autoincrement=True)
    role_name= Column(String(), unique=True)



    def __repr__(self):
        return f'\n<id={self.id} name={self.name} role_name={self.role_name} >'

    def __str__(self):
        return f'\n<id={self.id} name={self.name} country_id={self.country_id} user_id={self.user_id} >'


