#!/usr/bin/env python3

"""THis module contains a database table mapped with sqlAlchemy
"""

from typing import Optional
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class User(Base):
    """This is the user class mapped to the user
    table in the database
    """
    __tablename__: str = "users"

    id: int = Column(Integer, primary_key=True)
    email: str = Column(String(250))
    hashed_password: str = Column(String(250), nullable=False)
    session_id: Optional[str] = Column(String(250))
    reset_token: Optional[str] = Column(String(250))
