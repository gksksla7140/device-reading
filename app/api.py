from fastapi import APIRouter
from .models import DeviceReadings, FetchReadingsResponse, StoreReadingsResponse
from .storage import readings_storage


router = APIRouter()

@router.post("/store_readings/")
async def store_readings_endpoint(readings_data: DeviceReadings) -> StoreReadingsResponse:
    device_id = readings_storage.store_readings(readings_data)
    success_message = f"Readings for Device ID {device_id} have been successfully stored."
    return StoreReadingsResponse(message=success_message)

@router.get("/fetch_readings/{device_id}")
async def fetch_readings_endpoint(device_id: str) -> FetchReadingsResponse:
    readings = readings_storage.fetch_readings(device_id)
    return FetchReadingsResponse(readings=readings)
