#!/usr/bin/python3
"""
This script list all Stae object that contains
the letter 'a' from the database `hbtn_0e_6_usa`.
"""

from sys import argv
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    """
    Acces to the database and get
    a state from the database
    """

    db_url = "mysal+mysqldb://{}:{}@localhost:3306/{}".format(
            argv[1], argv[2], argv[3])
    engine = create_engine(db_url)
    session = sessionmaker(bind=engine)

    session = session()

    states = session.query(State).filter(State.name.contains('a'))
    if state is not None:
        for state in states:
            print('{0}: {1}'.format(state.id, state.name))
