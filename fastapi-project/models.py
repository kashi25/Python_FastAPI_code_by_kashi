from sqlalchemy import (Column, Date, Float, Integer, Boolean, ForeignKey,
                        String, DateTime)
from sqlalchemy.dialects.postgresql import UUID
from config import Base

from sqlalchemy.orm import relationship
from sqlalchemy_utils import URLType
from datetime import datetime


# This class holds user_basic informations
class UserTable(Base):
    __tablename__ = 'user_basic'

    id = Column(UUID(as_uuid=True), primary_key=True)
    email = Column(String(255))
    first_name = Column(String(255))
    last_name = Column(String(255))
    profile_pic = Column(URLType)
    is_verified = Column(Boolean)
    auth_provider = Column(String(255))
    is_active = Column(Boolean)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    Rel1 = relationship("PatientTable",  back_populates="Rel2")

    # patient_info = relationship("PatientTable", back_populates="users")


# This class holds patient informations
class PatientTable(Base):
    __tablename__ = 'patient_info'

    id = Column(UUID(as_uuid=True), primary_key=True)
    user_id = Column(UUID(as_uuid=True), ForeignKey('user_basic.id',
                                                    ondelete='CASCADE'))
    phone_number = Column(String)
    address = Column(String(255))
    birth_date = Column(Date)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    Rel2 = relationship("UserTable", back_populates="Rel1")
    Rel4 = relationship("Pain_Patient_class", back_populates="Rel3")

# Hold Pain_patient details information


class Pain_Patient_class(Base):
    __tablename__ = "pain_patient_map"
    id = Column(UUID(as_uuid=True), primary_key=True)
    pain_history_id = Column(UUID(as_uuid=True))
    patient_id = Column(UUID(as_uuid=True), ForeignKey('patient_info.id',
                                                       ondelete='CASCADE'))
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    Rel3 = relationship("PatientTable", back_populates="Rel4")
    Rel6 = relationship("Pain_History_class", back_populates="Rel5")


# holds the pain_history information
class Pain_History_class(Base):
    __tablename__ = "pain_history"
    id = Column(UUID(as_uuid=True), primary_key=True)
    painhistory_id = Column(UUID(as_uuid=True),
                                 ForeignKey('pain_patient_map.id',
                                            ondelete='CASCADE'))
    type_of_pain = Column(String)
    nature_of_pain = Column(String)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    Rel5 = relationship("Pain_Patient_class", back_populates="Rel6")
