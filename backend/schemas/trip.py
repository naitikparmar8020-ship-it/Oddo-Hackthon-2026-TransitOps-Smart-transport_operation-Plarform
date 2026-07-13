from pydantic import BaseModel

class TripBase(BaseModel):
    source: str
    destination: str
    vehicle_id: int
    driver_id: int
    cargo_weight: int
    planned_distance: float
    status: str = "Draft"

class TripCreate(TripBase):
    pass

class TripResponse(TripBase):
    id: int

    class Config:
        from_attributes = True