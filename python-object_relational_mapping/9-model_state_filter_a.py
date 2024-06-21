#!/usr/bin/python3
"""
Lists all State objects that contain the letter 'a' from
the database hbtn_0e_6_usa
"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]

    connection_string = "mysql+mysqldb://{}:{}@localhost/{}".format(mysql_username, mysql_password, db_name)

    engine = create_engine(connection_string, pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    states_with_a = session.query(State).filter(State.name.like('%a%')).order_by(State.id).all()

    for state in states_with_a:
        print(f"{state.id}: {state.name}")

    session.close()
