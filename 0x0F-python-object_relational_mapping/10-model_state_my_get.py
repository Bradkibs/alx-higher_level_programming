#!/usr/bin/python3
"""
a python script that prints the id of a given state when passed on
in the commandline as input or Nothing if the name doesn't exist
Example: ./10-model_state_my_get.py root root hbtn_0e_6_usa Texas
3
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
    Session = sessionmaker(bind=db_engine)
    sess_obj = Session()
    query = sess_obj.query(State).filter(State.name == (argv[4],))
    try:
        print(query[0].id)
    except IndexError:
        print("Not found")
