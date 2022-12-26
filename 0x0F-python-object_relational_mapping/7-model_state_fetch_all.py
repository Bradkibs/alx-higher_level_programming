#!/usr/bin/python3
"""
a python script that lists all state objects from the database
using sqlalchemy
"""


from model_state import State, Base
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    url_params = {'drivername': 'mysql+mysqldb',
                  'username': argv[1],
                  'password': argv[2],
                  'host': 'localhost',
                  'port': 3306,
                  'database': argv[3]}
    db_engine = create_engine(URL.create(**url_params))
    Base.metadata.create_all(db_engine)
    Session = sessionmaker(bind=db_engine)()
    for row in Session.query(State).order_by(State.id):
        print(row.id, row.name, sep=": ")
