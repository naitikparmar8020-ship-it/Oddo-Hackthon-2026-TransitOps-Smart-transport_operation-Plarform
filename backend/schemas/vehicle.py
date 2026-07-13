from pydantic import BaseModel

class VehicleBase(BaseModel):
    registration_number: str
    name: str
    vehicle_type: str
    max_load_capacity: int
    odometer: int = 0
    acquisition_cost: int
    status: str = "Available"

class VehicleCreate(VehicleBase):
    pass

class VehicleResponse(VehicleBase):
    id: int

    class Config:
        from_attributes = True