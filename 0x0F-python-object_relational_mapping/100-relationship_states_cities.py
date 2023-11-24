#!/usr/bin/python3
"""Import modules for script."""
import sys
from relationship_city import City
from relationship_state import Base, State
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
    city = City(name='San Francisco')
    state = State(name='California')
    state.cities.append(city)
    sesh.add(state)
    sesh.commit()
    sesh.close()
