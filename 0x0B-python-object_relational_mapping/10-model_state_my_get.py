#!/usr/bin/python3
"""
print the State Objects
with name passed as argument using SQLAlchemy
"""
from model_state import Base, State
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == '__main__':
    user = sys.argv[1]
    passwrd = sys.argv[2]
    db = sys.argv[3]

    db_url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'\
        .format(user, passwrd, db)

    engine = create_engine(db_url, pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).filter(State.name == sys.arg[4]).first()
    if states:
        print('{}'.format(states.id))
    else:
        print("Not found")
    session.close()
