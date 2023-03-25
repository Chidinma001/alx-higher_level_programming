#!/usr/bin/python3
"""A module called 10-model_state_my_get"""
import sys
from model_state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    instances = session.query(State).filter(State.name.like(sys.argv[4]))
    first_instance = instances.first()
    try:
        print(first_instance.id)
    except AttributeError:
        print("Not found")
