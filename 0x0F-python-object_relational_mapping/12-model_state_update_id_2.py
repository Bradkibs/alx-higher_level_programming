#!/usr/bin/python3
"""
a python script that updates the name of a State object from the database
It changes the name of the State where id = 2 to New Mexico
"""


from model_state import State, Base
from sys import argv
from sqlalchemy import create_engine, insert
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    url_params = {'drivername': 'mysql+mysqldb',
                  'username': argv[1],
                  'password': argv[2],
                  'host': 'localhost',
                  'port': 3306,
                  'database': argv[3]}
    db_engine = create_engine(URL.create(**url_params), echo=True)
    Base.metadata.create_all(db_engine)
    Session = sessionmaker(bind=db_engine)
    sess_obj = Session()
    q = sess_obj.query(State).filter(State.id == 2)\
                .update({'name': "New Mexico"})
    sess_obj.commit()
