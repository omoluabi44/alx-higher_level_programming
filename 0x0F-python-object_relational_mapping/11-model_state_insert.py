#!/usr/bin/python3
"""  lists all states from the database hbtn_0e_0_usa """
import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    usrnm = sys.argv[1]
    usrpsw = sys.argv[2]
    dbnm = sys.argv[3]
    stnm = sys.argv[4]

    connection_string = 'mysql+mysqldb://{}:{}@localhost:3306/{}'\
        .format(usrnm, usrpsw, dbnm)
    engine = create_engine(connection_string)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    new_state = State(name='Louisiana')
    session.add(new_state)
    new_instance = session.query(State).filter_by(name='Louisiana').first()
    print(new_instance.id)
    session.commit()
