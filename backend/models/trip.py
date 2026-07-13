from sqlalchemy import Column, Integer, String, Float, ForeignKey
from database import Base

class Trip(Base):
    __tablename__ = "trips"

    id = Column(Integer, primary_key=True, index=True)
    source = Column(String)
    destination = Column(String)
    vehicle_id = Column(Integer, ForeignKey("vehicles.id"))
    driver_id = Column(Integer, ForeignKey("drivers.id"))
    cargo_weight = Column(Integer)
    planned_distance = Column(Float)
    status = Column(String, default="Draft") # Draft, Dispatched, Completed, Cancelled