#!/usr/bin/python3
"""
a python script that deletes all State objects with a name
containing the letter 'a'
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
    q = sess_obj.query(State).filter(State.name.like('%a%'))\
                .delete(synchronize_session='fetch')
    sess_obj.commit()
