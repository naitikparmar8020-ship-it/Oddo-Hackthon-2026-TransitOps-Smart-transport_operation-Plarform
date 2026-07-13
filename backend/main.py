from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
from database import get_db, engine
import models
from routers import vehicles_router, drivers_router, trips_router, maintenance_router, fuel_router

# Build the database tables from our new models folder
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="TransitOps API")

# Include our new professional routers
app.include_router(vehicles_router)
app.include_router(drivers_router)
app.include_router(trips_router)
app.include_router(maintenance_router)
app.include_router(fuel_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the TransitOps API!"}

@app.get("/test-db")
def test_database_connection(db: Session = Depends(get_db)):
    try:
        db.execute(text("SELECT 1"))
        return {"status": "success", "message": "Database connected perfectly!"}
    except Exception as e:
        return {"status": "error", "message": str(e)}