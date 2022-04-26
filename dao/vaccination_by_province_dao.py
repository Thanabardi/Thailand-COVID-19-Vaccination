import datetime
from vaccination_by_province import VaccByDose, VaccByAuth
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, func

engine = create_engine('sqlite:///vaccination_by_province.db')
Session = sessionmaker(bind=engine)
session = Session()


def format_data_auth(d):
    return (d.id, d.province, d.total_doses, d.AstraZeneca, d.Sinovac, d.Sinopharm, d.Pfizer, d.Johnson_Johnson, d.date.strftime("%d/%m/%Y, %H:%M:%S"))


def get_query_auth():
    data = session.query(VaccByAuth)
    list = []
    for d in data:
        list.append(format_data_auth(d))
    return list


def get_query_auth_by_province(province: str):
    try:
        d = session.query(VaccByAuth).filter(func.lower(
            VaccByAuth.province) == func.lower(province)).first()
        return f"id: {d.id}, Province: {d.province}, Total doses: {d.total_doses}, AstraZeneca: {d.AstraZeneca}, Sinovac: {d.Sinovac}, Sinovac: {d.Sinopharm}, Pfizer: {d.Pfizer}, Johnson&Johnson: {d.Johnson_Johnson}, Last updated: {d.date.strftime('%d/%m/%Y, %H:%M:%S')}"
        # return format_data_auth(d)
    except:
        return "Province Data Not Found"


def update_auth_by_province(province: str, total_doses: int, AstraZeneca: int, Sinovac: int, Sinopharm: int, Pfizer: int, Johnson_Johnson: int):
    try:
        update_data = session.query(VaccByAuth).filter(
            func.lower(VaccByAuth.province) == func.lower(province)).first()
        update_data.total_doses = total_doses
        update_data.AstraZeneca = AstraZeneca
        update_data.Sinovac = Sinovac
        update_data.Sinopharm = Sinopharm
        update_data.Pfizer = Pfizer
        update_data.Johnson_Johnson = Johnson_Johnson
        update_data.date = datetime.datetime.now()
        session.commit()
        return f"Update Success at {province} province"
    except:
        return f"Update Error"


def format_data_dose(d):
    return (d.id, d.province, d.over_60_1st_dose, d.total_1st_dose, d.total_2nd_dose, d.total_3rd_dose, d.date.strftime("%d/%m/%Y, %H:%M:%S"))


def get_query_dose():
    data = session.query(VaccByDose)
    list = []
    for d in data:
        list.append(format_data_dose(d))
    return list


def get_query_dose_by_province(province: str):
    try:
        d = session.query(VaccByDose).filter(func.lower(
            VaccByDose.province) == func.lower(province)).first()
        return f"id: {d.id}, Province: {d.province}, Age over 60 1st dose: {d.over_60_1st_dose}, Total 1st dose: {d.total_1st_dose}, Total 2nd dose: {d.total_2nd_dose}, Total 3rd dose: {d.total_3rd_dose}, Last updated: {d.date.strftime('%d/%m/%Y, %H:%M:%S')}"
        # return format_data_dose(d)
    except:
        return "Province Data Not Found"


def update_dose_by_province(province: str, over_60_1st_dose: int, total_1st_dose: int, total_2nd_dose: int, total_3rd_dose: int):
    try:
        update_data = session.query(VaccByDose).filter(
            func.lower(VaccByDose.province) == func.lower(province)).first()
        update_data.over_60_1st_dose = over_60_1st_dose
        update_data.total_1st_dose = total_1st_dose
        update_data.total_2nd_dose = total_2nd_dose
        update_data.total_3rd_dose = total_3rd_dose
        update_data.date = datetime.datetime.now()
        session.commit()
        return f"Update Success at {province} province"
    except:
        return f"Update Error"
