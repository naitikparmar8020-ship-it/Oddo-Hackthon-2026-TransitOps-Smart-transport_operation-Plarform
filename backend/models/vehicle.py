from sqlalchemy import Column, Integer, String, Boolean
from database import Base

class Vehicle(Base):
    __tablename__ = "vehicles"

    id = Column(Integer, primary_key=True, index=True)
    registration_number = Column(String, unique=True, index=True) # Enforcing unique rule!
    name = Column(String, index=True)
    vehicle_type = Column(String)
    max_load_capacity = Column(Integer)
    odometer = Column(Integer, default=0)
    acquisition_cost = Column(Integer)
    status = Column(String, default="Available") # Available, On Trip, In Shop, Retired