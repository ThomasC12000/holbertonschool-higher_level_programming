#!/usr/bin/python3
"""
Prints all City objects from the database hbtn_0e_14_usa.
"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]

    connection_string = f"mysql+mysqldb://{mysql_username}:{mysql_password}@localhost/{db_name}"

    engine = create_engine(connection_string, pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    results = session.query(State, City).filter(State.id == City.state_id).order_by(City.id).all()

    for state, city in results:
        print(f"{state.name}: ({city.id}) {city.name}")

    session.close()
