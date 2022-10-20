#!/usr/bin/python3
"""
update State object where id=2 in database to 'New Mexico'
using SQLAlchemy
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
    name_update = session.query(State).filter_by(id=2).first()
    name_update.name = "New Mexico"
    session.commit()
    session.close()
