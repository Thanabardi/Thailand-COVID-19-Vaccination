# from requests import Session
from sqlalchemy import Column, create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import pandas as pd
from config import *

Base = declarative_base()


class VaccByDose(Base):
    """create vaccination_by_dose table"""

    __tablename__ = "vaccination_by_dose"
    id = Column(Integer, primary_key=True, nullable=False)
    province = Column(String(50), nullable=False)
    over_60_1st_dose = Column(Integer, default=0)
    total_1st_dose = Column(Integer, default=0)
    total_2nd_dose = Column(Integer, default=0)
    total_3rd_dose = Column(Integer, default=0)
    date = Column(DateTime, nullable=False)


class VaccByAuth(Base):
    """create vaccination_by_authorizations table"""

    __tablename__ = "vaccination_by_authorizations"
    id = Column(Integer, primary_key=True, nullable=False)
    province = Column(String(50), nullable=False)
    total_doses = Column(Integer, default=0)
    AstraZeneca = Column(Integer, default=0)
    Sinovac = Column(Integer, default=0)
    Sinopharm = Column(Integer, default=0)
    Pfizer = Column(Integer, default=0)
    Johnson_Johnson = Column(Integer, default=0)
    date = Column(DateTime, nullable=False)


if __name__ == "__main__":
    # create the database
    engine = create_engine(URLI)
    Base.metadata.create_all(engine)

    # create the session
    session = sessionmaker()
    session.configure(bind=engine)
    s = session()

    try:
        # add vaccination_by_dose table data
        file_name = 'data/vaccination_by_dose.csv'
        df = pd.read_csv(file_name)
        df.to_sql(con=engine, index=False,
                  name=VaccByDose.__tablename__, if_exists='replace')

        # add vaccination_by_authorizations table data
        file_name = 'data/vaccination_by_authorizations.csv'
        df = pd.read_csv(file_name)
        df.to_sql(con=engine, index=False,
                  name=VaccByAuth.__tablename__, if_exists='replace')
    except:
        s.rollback()  # rollback the changes on error
