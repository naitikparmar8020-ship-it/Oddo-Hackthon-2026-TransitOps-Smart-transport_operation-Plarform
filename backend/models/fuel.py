from sqlalchemy import Column, Integer, Float, ForeignKey, Date, String
from database import Base

class FuelLog(Base):
    __tablename__ = "fuel_logs"

    id = Column(Integer, primary_key=True, index=True)
    vehicle_id = Column(Integer, ForeignKey("vehicles.id"))
    date = Column(Date)
    volume_liters = Column(Float)
    cost = Column(Float)
    odometer_reading = Column(Integer)
    receipt_number = Column(String, nullable=True)