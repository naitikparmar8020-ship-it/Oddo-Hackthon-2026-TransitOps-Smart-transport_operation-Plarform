from sqlalchemy import Column, Integer, String, Float, Date
from database import Base

class Driver(Base):
    __tablename__ = "drivers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    license_number = Column(String, unique=True, index=True)
    license_category = Column(String)  # e.g., Heavy Motor Vehicle, Light Motor Vehicle
    license_expiry_date = Column(Date)
    contact_number = Column(String)
    safety_score = Column(Float, default=5.0)  # Standard safety rating scale
    status = Column(String, default="Available")  # Available, On Trip, Off Duty, Suspended