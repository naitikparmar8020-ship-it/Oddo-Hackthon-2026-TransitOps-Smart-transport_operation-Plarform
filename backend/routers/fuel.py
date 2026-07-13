from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
import models
import schemas

router = APIRouter(
    prefix="/fuel",
    tags=["Fuel & Expenses"]
)

@router.post("/", response_model=schemas.FuelResponse)
def create_fuel_log(fuel: schemas.FuelCreate, db: Session = Depends(get_db)):
    # 1. Fetch the vehicle
    vehicle = db.query(models.Vehicle).filter(models.Vehicle.id == fuel.vehicle_id).first()
    
    if not vehicle:
        raise HTTPException(status_code=404, detail="Vehicle not found")

    # 2. MANDATORY RULE: Odometer reading cannot go backward!
    if fuel.odometer_reading < vehicle.odometer:
        raise HTTPException(
            status_code=400, 
            detail=f"Invalid reading! The vehicle's current odometer is already at {vehicle.odometer}."
        )

    # 3. Update the vehicle's master odometer automatically
    vehicle.odometer = fuel.odometer_reading

    # 4. Save the fuel log and the vehicle update
    db_fuel = models.FuelLog(**fuel.model_dump())
    db.add(db_fuel)
    db.commit()
    db.refresh(db_fuel)
    
    return db_fuel

@router.get("/", response_model=list[schemas.FuelResponse])
def get_fuel_logs(db: Session = Depends(get_db)):
    return db.query(models.FuelLog).all()