# from audioop import add
from datetime import date
from uuid import UUID
from sqlalchemy.orm import Session
from yarl import URL
from models import (PatientTable, UserTable,
                    Pain_History_class, Pain_Patient_class)
import models


# USER TABLE
# Creating function to get information of all users
def get_user(db: Session):
    return db.query(UserTable).all()


# Creating fuction to get information of user by userID
def get_user_by_id(db: Session, user_id: UUID):
    return db.query(UserTable).filter(UserTable.id == user_id).first()


# Creating function to create user and add it to the database and commit it
def create_user(db: Session, id: UUID, email: str, first_name: str,
                last_name: str, is_verified: bool, auth_provider: str,
                is_active: bool, profile_pic: str):
    db_user = models.UserTable(id=id, email=email, first_name=first_name,
                               last_name=last_name, is_verified=is_verified,
                               auth_provider=auth_provider,
                               is_active=is_active,
                               profile_pic=profile_pic)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


# Creating function to remove  user by userID
def remove_user(db: Session, user_id: UUID):
    _user = get_user_by_id(db=db, user_id=user_id)
    db.delete(_user)
    db.commit()


# Creating function to update user informations
def update_user(db: Session, user_id: UUID, email: str, first_name: str,
                last_name: str, is_verified: bool, auth_provider: bool,
                is_active: bool, profile_pic: str):
    _user = get_user_by_id(db=db, user_id=user_id)
    _user.email = email
    _user.first_name = first_name
    _user.last_name = last_name
    _user.is_verified = is_verified
    _user.profile_pic = profile_pic
    _user.auth_provider = auth_provider
    _user.is_active = is_active

    db.commit()
    db.refresh(_user)
    return _user


# PATIENT TABLE
# Creating function to get information of all patient
def get_patient(db: Session):
    return db.query(PatientTable).all()


# Creating funciton to get information of patient by patientID
def get_patient_by_id(db: Session, patient_id: UUID):
    return db.query(PatientTable).filter(PatientTable.id == patient_id).first()


# Creating function to create patient
def create_patient(db: Session, id: UUID, user_id: UUID, phone_number: str,
                   address: str, birth_date: date):
    db_patient = models.PatientTable(id=id, user_id=user_id,
                                     phone_number=phone_number,
                                     address=address,
                                     birth_date=birth_date)

    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    return db_patient


# Creating function to remove pationt using patientID
def remove_patient(db: Session, patient_id: UUID):
    _patient = get_patient_by_id(db=db, patient_id=patient_id)
    db.delete(_patient)
    db.commit()


# creating function to update patient Informaiton
def update_patient(db: Session, id: UUID, user_id: UUID, phone_number: str,
                   address: str, birth_date: date):
    _patient = get_patient_by_id(db=db, patient_id=id)
    _patient.id = user_id
    _patient.phone_number = phone_number
    _patient.address = address
    _patient.birth_date = birth_date

    db.commit()
    db.refresh(_patient)
    return _patient


# creating crud for Pain_patient_class

def get_pain_patient(db: Session):
    return db.query(PatientTable).all()


# Creating funciton to get information of pain by pain_patient_map id
def get_pain_patient_by_id(db: Session, id: UUID):
    return db.query(Pain_Patient_class).filter(Pain_Patient_class.id == id).first()


# Creating function to create pain_patient
def create_pain_patient(db: Session, id: UUID,
                        pain_history_id: UUID, patient_id: UUID):
    db_pain_patient = models.Pain_Patient_class(id=id,
                                                patient_id=patient_id,
                                                pain_history_id=pain_history_id)

    db.add(db_pain_patient)
    db.commit()
    db.refresh(db_pain_patient)
    return db_pain_patient

# Creating function to remove pain_patient using pain_patient id


def remove_pain_patient(db: Session, id: UUID):
    _pain_patient = get_pain_patient_by_id(db=db, id=id)
    db.delete(_pain_patient)
    db.commit()


# creating function to update pain_patient Informaiton
def update_pain_patient(db: Session, id: UUID,
                        patient_id: UUID, pain_history_id: UUID):
    _pain_patient = get_pain_patient_by_id(db=db, id=id)
    _pain_patient.id = id
    _pain_patient.pain_history_id = pain_history_id
    _pain_patient.patient_id = patient_id

    db.commit()
    db.refresh(_pain_patient)
    return _pain_patient


# creating crud for Pain_history_class

def get_pain_history(db: Session):
    return db.query(Pain_History_class).all()


# Creating funciton to get information of pain by pain_patient_map id
def get_pain_pain_history_by_id(db: Session, id: UUID):
    return db.query(Pain_History_class).filter(Pain_History_class.id == id).first()


# Creating function to create pain_history
def create_pain_history(db: Session, id: UUID, type_of_pain: str,
                        painhistory_id: UUID, nature_of_pain: str):
    db_pain_history = models.Pain_History_class(id=id,
                                                painhistory_id=painhistory_id,
                                                type_of_pain=type_of_pain,
                                                nature_of_pain=nature_of_pain)

    db.add(db_pain_history)
    db.commit()
    db.refresh(db_pain_history)
    return db_pain_history


# Creating function to remove pain_history using pain_history id


def remove_pain_history(db: Session, id: UUID):
    _pain_history = get_pain_pain_history_by_id(db=db, id=id)
    db.delete(_pain_history)
    db.commit()

# creating function to update pain_history Informaiton


def update_pain_history(db: Session, id: UUID, painhistory_id: UUID,
                        type_of_pain: str, nature_of_pain: str):
    _pain_history = get_pain_pain_history_by_id(db=db, id=id)
    _pain_history.id = id
    _pain_history.painhistory_id = painhistory_id
    _pain_history.type_of_pain = type_of_pain
    _pain_history.nature_of_pain = nature_of_pain

    db.commit()
    db.refresh(_pain_history)
    return _pain_history
