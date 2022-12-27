#!/usr/bin/python3
"""
Prints all City objects from the database hbtn_0e_14_usa
"""


from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)
    sess_obj = session()
    query = sess_obj.query(State.name, City.id, City.name)\
                    .where(State.id == City.state_id)\
                    .order_by(City.id)
    for row in query:
        print(row[0] + ": (" + str(row[1]) + ") " + row[2])
