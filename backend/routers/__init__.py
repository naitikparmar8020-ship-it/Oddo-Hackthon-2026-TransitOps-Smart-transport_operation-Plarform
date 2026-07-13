from routers.vehicles import router as vehicles_router
from routers.drivers import router as drivers_router
from routers.trips import router as trips_router
from routers.maintenance import router as maintenance_router

__all__ = ["vehicles_router", "drivers_router", "trips_router","maintenance_router"]