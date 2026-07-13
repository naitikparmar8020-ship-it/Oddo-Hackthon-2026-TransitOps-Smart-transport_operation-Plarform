from sqlalchemy import Column, Integer, String, Float, ForeignKey, Boolean, Date
from database import Base

class Maintenance(Base):
    __tablename__ = "maintenance_logs"

    id = Column(Integer, primary_key=True, index=True)
    vehicle_id = Column(Integer, ForeignKey("vehicles.id"))
    description = Column(String)
    cost = Column(Float)
    start_date = Column(Date)
    end_date = Column(Date, nullable=True)
    is_open = Column(Boolean, default=True)