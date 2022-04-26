import datetime
from abc import ABC, abstractmethod
from vaccination_by_province import VaccByDose, VaccByAuth
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, func
from config import *


class Dao(ABC):
    def __init__(self, session):
        self._session = session

    @abstractmethod
    def format_data(self, d):
        pass

    @abstractmethod
    def get_query(self):
        pass

    @abstractmethod
    def get_query_by_province(self, province: str):
        pass

    @abstractmethod
    def update_by_province(self, data: dict):
        pass


class DoseDao(Dao):
    def format_data(self, d):
        return (d.id, d.province, d.over_60_1st_dose, d.total_1st_dose, d.total_2nd_dose, d.total_3rd_dose, d.date.strftime("%d/%m/%Y, %H:%M:%S"))

    def get_query(self):
        data = self._session.query(VaccByDose)
        list = []
        for d in data:
            list.append(self.format_data(d))
        return list

    def get_query_by_province(self, province: str):
        try:
            d = self._session.query(VaccByDose).filter(func.lower(
                VaccByDose.province) == func.lower(province)).first()
            return f"id: {d.id}, Province: {d.province}, Age over 60 1st dose: {d.over_60_1st_dose}, Total 1st dose: {d.total_1st_dose}, Total 2nd dose: {d.total_2nd_dose}, Total 3rd dose: {d.total_3rd_dose}, Last updated: {d.date.strftime('%d/%m/%Y, %H:%M:%S')}"
            # return format_data_dose(self, d)
        except:
            return "Province record Not Found"

    def update_by_province(self, data: dict):
        try:
            date = datetime.datetime.now()
            update_data = self._session.query(VaccByDose).filter(
                func.lower(VaccByDose.province) == func.lower(data["province"])).first()
            update_data.over_60_1st_dose = data["over_60_1st_dose"]
            update_data.total_1st_dose = data["total_1st_dose"]
            update_data.total_2nd_dose = data["total_2nd_dose"]
            update_data.total_3rd_dose = data["total_3rd_dose"]
            update_data.date = date
            self._session.commit()
            return f"{data['province']} province record successfully updated at {date.strftime('%d/%m/%Y, %H:%M:%S')}"
        except:
            return f"Update Error"


class AuthDao(Dao):

    def format_data(self, d):
        return (d.id, d.province, d.total_doses, d.AstraZeneca, d.Sinovac, d.Sinopharm, d.Pfizer, d.Johnson_Johnson, d.date.strftime("%d/%m/%Y, %H:%M:%S"))

    def get_query(self):
        data = self._session.query(VaccByAuth)
        list = []
        for d in data:
            list.append(self.format_data(d))
        return list

    def get_query_by_province(self, province: str):
        try:
            d = self._session.query(VaccByAuth).filter(func.lower(
                VaccByAuth.province) == func.lower(province)).first()
            return f"id: {d.id}, Province: {d.province}, Total doses: {d.total_doses}, AstraZeneca: {d.AstraZeneca}, Sinovac: {d.Sinovac}, Sinovac: {d.Sinopharm}, Pfizer: {d.Pfizer}, Johnson&Johnson: {d.Johnson_Johnson}, Last updated: {d.date.strftime('%d/%m/%Y, %H:%M:%S')}"
            # return format_data_auth(self, d)
        except:
            return "Province record Not Found"

    def update_by_province(self, data: dict):
        try:
            date = datetime.datetime.now()
            update_data = self._session.query(VaccByAuth).filter(
                func.lower(VaccByAuth.province) == func.lower(data["province"])).first()
            update_data.total_doses = data["total_doses"]
            update_data.AstraZeneca = data["AstraZeneca"]
            update_data.Sinovac = data["Sinovac"]
            update_data.Sinopharm = data["Sinopharm"]
            update_data.Pfizer = data["Pfizer"]
            update_data.Johnson_Johnson = data["Johnson_Johnson"]
            update_data.date = date
            self._session.commit()
            return f"{data['province']} province record successfully updated at {date.strftime('%d/%m/%Y, %H:%M:%S')}"
        except:
            return f"Update Error"


class DaoFactory():
    def __init__(self, table: str):
        self._engine = create_engine(URLI)
        self._Session = sessionmaker(bind=self._engine)
        self._session = self._Session()
        self._table = table

    def create_dao(self):
        if (self._table == 'dose'):
            return DoseDao(self._session)
        elif (self._table == 'auth'):
            return AuthDao(self._session)
