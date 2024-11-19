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
    __table_args__ = {'sqlite_autoincrement': True}

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    email: str = Column(String(250), nullable=False)
    hashed_password: str = Column(String(250), nullable=False)
    session_id: Optional[str] = Column(String(250), nullable=True)
    reset_token: Optional[str] = Column(String(250), nullable=True)
