from fastapi import APIRouter

router = APIRouter()

@router.post("/store_readings/")
async def store_readings_endpoint():
    pass

@router.get("/fetch_readings/{device_id}")
async def fetch_readings_endpoint(device_id: str):
    pass