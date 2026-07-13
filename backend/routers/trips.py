from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
import models
import schemas

router = APIRouter(
    prefix="/trips",
    tags=["Trips"]
)

@router.post("/", response_model=schemas.TripResponse)
def create_trip(trip: schemas.TripCreate, db: Session = Depends(get_db)):
    # 1. Fetch the requested vehicle and driver from the database
    vehicle = db.query(models.Vehicle).filter(models.Vehicle.id == trip.vehicle_id).first()
    driver = db.query(models.Driver).filter(models.Driver.id == trip.driver_id).first()

    # Ensure they exist
    if not vehicle:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    if not driver:
        raise HTTPException(status_code=404, detail="Driver not found")

    # 2. MANDATORY RULE: Check Load Capacity
    if trip.cargo_weight > vehicle.max_load_capacity:
        raise HTTPException(
            status_code=400, 
            detail=f"Cargo weight ({trip.cargo_weight}kg) exceeds vehicle capacity ({vehicle.max_load_capacity}kg)."
        )

    # 3. MANDATORY RULE: Check Availability Status
    if vehicle.status != "Available":
        raise HTTPException(status_code=400, detail="Vehicle is not available for dispatch.")
    if driver.status != "Available":
        raise HTTPException(status_code=400, detail="Driver is not available for dispatch.")

    # 4. Save the trip to the database
    db_trip = models.Trip(**trip.model_dump())
    db.add(db_trip)
    db.commit()
    db.refresh(db_trip)
    return db_trip

@router.get("/", response_model=list[schemas.TripResponse])
def get_trips(db: Session = Depends(get_db)):
    return db.query(models.Trip).all()