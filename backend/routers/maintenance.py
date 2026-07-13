from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
import models
import schemas

router = APIRouter(
    prefix="/maintenance",
    tags=["Maintenance"]
)

@router.post("/", response_model=schemas.MaintenanceResponse)
def create_maintenance(maint: schemas.MaintenanceCreate, db: Session = Depends(get_db)):
    # 1. Fetch the vehicle
    vehicle = db.query(models.Vehicle).filter(models.Vehicle.id == maint.vehicle_id).first()
    
    if not vehicle:
        raise HTTPException(status_code=404, detail="Vehicle not found")

    # 2. MANDATORY RULE: Toggle vehicle status based on maintenance
    if maint.is_open:
        vehicle.status = "In Shop"
    else:
        # If maintenance is closed, restore status to Available (unless we later add logic for Retired)
        vehicle.status = "Available"

    # 3. Save the log and the updated vehicle status
    db_maint = models.Maintenance(**maint.model_dump())
    db.add(db_maint)
    db.commit()
    db.refresh(db_maint)
    
    return db_maint

@router.get("/", response_model=list[schemas.MaintenanceResponse])
def get_maintenance_logs(db: Session = Depends(get_db)):
    return db.query(models.Maintenance).all()