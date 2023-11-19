#!/usr/bin/python3
"""
Import modules for script.
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'.format(
                sys.argv[1],
                sys.argv[2],
                sys.argv[3]),
            pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    sesh = Session()
    change = sesh.query(State).filter(State.id == 2).first()
    change.name = "New Mexico"
    sesh.commit()
    sesh.close()
