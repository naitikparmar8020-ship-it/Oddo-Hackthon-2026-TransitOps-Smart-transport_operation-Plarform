from pydantic import BaseModel
from datetime import date
from typing import Optional

class FuelBase(BaseModel):
    vehicle_id: int
    date: date
    volume_liters: float
    cost: float
    odometer_reading: int
    receipt_number: Optional[str] = None

class FuelCreate(FuelBase):
    pass

class FuelResponse(FuelBase):
    id: int

    class Config:
        from_attributes = True