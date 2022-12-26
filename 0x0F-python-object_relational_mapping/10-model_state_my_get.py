#!/usr/bin/python3
"""
a python script that prints the first state object from the db
The results must be displayed as follows
1: California
or "Nothing" if the query returns nothing
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
