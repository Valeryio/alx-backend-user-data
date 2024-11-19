#!/usr/bin/env python3

"""THis module contains a database table mapped with sqlAlchemy
"""

from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class User(Base):
    """This is the user class mapped to the user
    table in the database
    """
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False, index=True)
    session_id = Column(String)
    reset_token = Column(String)
