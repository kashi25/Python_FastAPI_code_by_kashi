from datetime import date
import shutil
from uuid import UUID
from fastapi import APIRouter, File, UploadFile
from fastapi import Depends
from fastapi_sqlalchemy import db
from config import SessionLocal
from sqlalchemy.orm import Session
from schemas import (
                      RequestPatient, RequestPain_Patient,
                      RequestUser, RequestPainhistory, Response)

import crud

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# USER TABLE Routes
# Defining path operation for /user/create
@router.post("/user/create")
async def create_user_service(id: UUID, email: str, first_name: str,
                              last_name: str, is_verified: bool,
                              auth_provider: str, is_active: bool,
                              db: Session=Depends(get_db),
                              file: UploadFile=File(...)):
    with open("media/" + file.filename, "wb") as image:
        shutil.copyfileobj(file.file, image)
    url = str("media/" + file.filename)

    return crud.create_user(db=db, id=id, email=email, first_name=first_name,
                            last_name=last_name, is_verified=is_verified,
                            auth_provider=auth_provider, is_active=is_active,
                            profile_pic=url)


# Defining path operation for /user
@router.get("/user")
async def get_users(db: Session=Depends(get_db)):
    _users = crud.get_user(db)
    return Response(status="Ok", code="200", message="Success fetch all data",
                    result=_users)


# Defining path operation for /user/{userID}
@router.get("/user/{userID}")
async def get_by_user_id(id: UUID, db: Session=Depends(get_db)):
    _users = crud.get_user_by_id(db, id)
    return Response(status="OK", code=200, message="Success fetch with id",
                    result=_users)


# Defining path operation for /user/update
@router.patch("/user/update/")
async def update_user(id: UUID, email: str, first_name: str, last_name: str,
                      is_verified: bool, auth_provider: str, is_active: bool,
                      db: Session=Depends(get_db),
                      file: UploadFile=File(...)):
    with open("media/updated/"+file.filename, "wb") as image:
        shutil.copyfileobj(file.file, image)
    url = str("media/updated/"+file.filename)

    return crud.update_user(db=db, email=email, first_name=first_name,
                            last_name=last_name, is_verified=is_verified,
                            auth_provider=auth_provider, is_active=is_active,
                            profile_pic=url, user_id=id)


# Defining path operation for /user/delete
@router.delete("user/delete")
async def delete_user(request: RequestUser,  db: Session=Depends(get_db)):
    crud.remove_user(db, user_id=request.parameter.id)
    return Response(status="Ok", code="200",
                    message="Success delete data").dict(exclude_none=True)


# PATIENT TABLE
# Defining path operation for /patient/create
@router.post("/patient/create")
async def create_patient_service(id: UUID, user_id: UUID,
                                 phone_number: str, address: str,
                                 birth_date: date,
                                 db: Session=Depends(get_db)):
    return crud.create_patient(db=db, id=id, user_id=user_id,
                               phone_number=phone_number, address=address,
                               birth_date=birth_date)


# Defining path operation for /patient
@router.get("/patient")
async def get_patient(db: Session=Depends(get_db)):
    _patients = crud.get_patient(db)
    return Response(status="OK", code="200",
                    message="Success fetch all data of patient",
                    result=_patients)


# Defining path operation for /patient/{patientID}
@router.get("/patient/{patientID}")
async def get_by_patient_id(id: UUID, db: Session=Depends(get_db)):
    _patient = crud.get_patient_by_id(db, id)
    return Response(status="OK", code=200,
                    message="Success fetch data with id", result=_patient)


# Defining path operation for /patient/update
@router.patch("/patient/update")
async def update_patient(id: UUID, user_id: UUID, phone_number: str,
                         address: str, birth_date: date,
                         db: Session=Depends(get_db)):
    return crud.update_patient(db=db, id=id, user_id=user_id,
                               phone_number=phone_number,
                               address=address, birth_date=birth_date)


# Defining path operation for /patient/delete
@router.delete("/patient/delete")
async def delete_patient(request: RequestPatient,
                         db: Session=Depends(get_db)):
    crud.remove_patient(db, patient_id=request.parameter.id)
    return Response(status="Ok", code="200",
                    message="Success delete data").dict(exclude_none=True)


# routing path for pain_patient
@router .get("/pain_patient")
async def get_pain_patient(db: Session=Depends(get_db)):
    _pain_patient = crud.get_pain_patient(db)
    return Response(status="OK", code="200",
                    message="Success fetch all data of patient",
                    result=_pain_patient)

# Defining path operation for /pain_patient/{pain_patient ID}


@router.get("/pain_patient/{patientID}")
async def get_pain_patient_by_id(id: UUID, db: Session=Depends(get_db)):
    _patient = crud.get_pain_patient_by_id(db, id)
    return Response(status="OK", code=200,
                    message="Success fetch data with id", result=_patient)


# Defining path operation for /pain_patient/update
@router.patch("/pain_patient/update")
async def update_pain_patient(id: UUID, patient_id: UUID,
                              pain_history_id: UUID,
                              db: Session=Depends(get_db)):
    return crud.update_pain_patient(db=db, id=id, patient_id=patient_id,
                                    pain_history_id=pain_history_id)


# Defining path operation for /pain_patient/delete
@router.delete("/pain_patinet/delete")
async def delete_patient(request: RequestPain_Patient,
                         db: Session=Depends(get_db)):
    crud.remove_pain_patient(db, id=request.parameter.id)
    return Response(status="Ok", code="200",
                    message="Success delete data").dict(exclude_none=True)

# post method for pain_patient


@router.post("/pain_patient/create")
async def create_pain_patient(id: UUID, pain_history_id: UUID,
                              patient_id: UUID,
                              db: Session=Depends(get_db)):
    return crud.create_pain_patient(db=db, id=id,
                                    pain_history_id=pain_history_id,
                                    patient_id=patient_id)

# routs for pain_history


@router .get("/pain_history")
async def get_pain_history(db: Session=Depends(get_db)):
    _pain_history = crud.get_pain_history(db)
    return Response(status="OK", code="200",
                    message="Success fetch all data of patient",
                    result=_pain_history)


# Defining path operation for /pain_history/{pain_patient ID}
@router.get("/pain_history/{pain_history ID}")
async def get_pain_pain_history_by_id(id: UUID, db: Session=Depends(get_db)):
    _patient = crud.get_pain_pain_history_by_id(db, id)
    return Response(status="OK", code=200,
                    message="Success fetch data with id", result=_patient)

# post method for pain_history


@router.post("/pain_history/create")
async def create_pain_history(id: UUID, painhistory_id: UUID,
                              type_of_pain: str,
                              nature_of_pain: str,
                              db: Session=Depends(get_db)):
    return crud.create_pain_history(db=db, id=id, type_of_pain=type_of_pain,
                                    nature_of_pain=nature_of_pain,
                                    painhistory_id=painhistory_id)

# delete method for pain_history


@router.delete("/pain_history/delete")
async def delete_pain_history(request: RequestPainhistory,
                              db: Session=Depends(get_db)):
    crud.remove_pain_history(db, id=request.parameter.id)
    return Response(status="Ok", code="200",
                    message="Success delete data").dict(exclude_none=True)

# patch method for pain history


@router.patch("/pain_history/update")
async def update_pain_history(id: UUID, painhistory_id: UUID,
                              type_of_pain: str,
                              nature_of_pain: str,
                              db: Session=Depends(get_db)):
    return crud.update_pain_history(db=db, id=id, type_of_pain=type_of_pain,
                                    nature_of_pain=nature_of_pain,
                                    painhistory_id=painhistory_id)
