from datetime import datetime
from sqlalchemy import Column, Integer,BigInteger, String, DateTime, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship, backref
from Db_config import Base

class Administrator(Base):
    __tablename__ = 'administrators'

    id = Column(BigInteger(), primary_key=True, autoincrement=True)
    first_name= Column(String())
    last_name=Column(String())
    user_id=Column(BigInteger(), ForeignKey ('users.id'),nullable=False, unique=True)

    admin_users=relationship('User',foreign_keys=[user_id], backref=backref("administrator_user", uselist=True))


    def __repr__(self):
        return f'\n<id={self.id} first_name={self.first_name} last_name={self.last_name} user_id={self.user_id} >'

    def __str__(self):
        return f'\n<id={self.id} first_name={self.first_name} last_name={self.last_name} user_id={self.user_id} >'

