from datetime import date
from typing import Optional, Generic, TypeVar
from uuid import UUID
from pydantic import BaseModel, Field
from pydantic.generics import GenericModel


T = TypeVar('T')


# build a schema using pydantic
# Properties required during User creation


class UserSchema(BaseModel):
    id: UUID
    email: str
    first_name: str
    last_name: str
    is_verified: bool
    auth_provider: str
    is_active: bool

    class Config:
        orm_mode = True


# Properties required during Patient creation


class PatientSchema(BaseModel):
    id: UUID
    user_id: UUID
    phone_number: str
    address: str
    birth_date: date

    class Config:
        orm_mode = True


# Properties required during pain_patient creation


class Pain_PatientSchema(BaseModel):
    id: UUID
    pain_history_id: UUID
    patient_id: UUID

# properties required during pain_history


class Pain_historySchema(BaseModel):
    id: UUID
    painhistory_id: UUID
    type_of_pain: str
    nature_of_pain: str


# Holds properties of Optional field


class Request(GenericModel, Generic[T]):
    parameter: Optional[T] = Field(...)


# Holds properties of UserSchema


class RequestUser(BaseModel):
    parameter: UserSchema = Field(...)


# Holds properties of PatientSchema


class RequestPatient(BaseModel):
    parameter: PatientSchema = Field(...)


# hold this properties of Pain_PatientSchema


class RequestPain_Patient(BaseModel):
    parameter:  Pain_PatientSchema = Field(...)

# holds properties of Pain_historySchema


class RequestPainhistory(BaseModel):
    parameter: Pain_historySchema = Field(...)

    
class Response(GenericModel, Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T]
