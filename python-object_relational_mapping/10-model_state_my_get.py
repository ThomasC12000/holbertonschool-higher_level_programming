#!/usr/bin/python3
"""
Prints the State object with the name passed as argument from the database hbtn_0e_6_usa.
"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]
    state_name_to_search = sys.argv[4]

    connection_string = "mysql+mysqldb://{}:{}@localhost/{}".format(mysql_username, mysql_password, db_name)

    engine = create_engine(connection_string, pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(State.name == state_name_to_search).first()

    if state:
        print(f"{state.id}")
    else:
        print("Not found")

    session.close()
