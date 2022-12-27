#!/usr/bin/python3
"""
using SQLAlchemy orm to make queries to mysqldb
"""


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, MetaData

Meta = MetaData()
Base = declarative_base(metadata=Meta)


class State(Base):
    """
    A class state to define a mapped class
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    name = Column(String(128), nullable=False)
