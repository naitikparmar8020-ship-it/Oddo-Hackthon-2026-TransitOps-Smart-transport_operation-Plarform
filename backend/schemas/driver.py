from pydantic import BaseModel
from datetime import date

class DriverBase(BaseModel):
    name: str
    license_number: str
    license_category: str
    license_expiry_date: date
    contact_number: str
    safety_score: float = 5.0
    status: str = "Available"

class DriverCreate(DriverBase):
    pass

class DriverResponse(DriverBase):
    id: int

    class Config:
        from_attributes = True