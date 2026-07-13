from pydantic import BaseModel
from datetime import date
from typing import Optional

class MaintenanceBase(BaseModel):
    vehicle_id: int
    description: str
    cost: float
    start_date: date
    end_date: Optional[date] = None
    is_open: bool = True

class MaintenanceCreate(MaintenanceBase):
    pass

class MaintenanceResponse(MaintenanceBase):
    id: int

    class Config:
        from_attributes = True