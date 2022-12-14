#!/usr/bin/python3
"""
a python script that inserts Louisiana into the states table
and prints out its id
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
    db_engine = create_engine(URL.create(**url_params))
    Base.metadata.create_all(db_engine)
    Session = sessionmaker(bind=db_engine)
    sess_obj = Session()
    stmt = State(name='Louisiana')
    sess_obj.add(stmt)
    sess_obj.commit()
    q = sess_obj.query(State).filter(State.name == "Louisiana")
    for item in q:
        print(item.id)
