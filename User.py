from datetime import datetime
from sqlalchemy import Column, Integer,BigInteger, String, DateTime, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship, backref
from Db_config import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(BigInteger(), primary_key=True, autoincrement=True)
    username= Column(String(), unique=True)
    password=Column(String())
    email=Column(String(), unique=True)
    user_role=Column(Integer, ForeignKey('user_roles.id', ondelete='CASCADE'), nullable=False)

    role=relationship('User_Roles', backref=backref('users', uselist=True, passive_deletes=True))


    def __repr__(self):
        return f'\n<id={self.id} username={self.username} password={self.password} email={self.email}\
         user_role={self.user_role} >'

    def __str__(self):
        return f'\n<id={self.id} username={self.username} password={self.password} email={self.email}\
         user_role={self.user_role} >'

