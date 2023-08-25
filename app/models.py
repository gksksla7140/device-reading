from pydantic import BaseModel
from typing import List
import datetime

class Reading(BaseModel):
    timestamp: datetime.datetime
    count: int

class DeviceReadings(BaseModel):
    id: str
    readings: List[Reading]

class StoreReadingsResponse(BaseModel):
    message: str

class FetchReadingsResponse(BaseModel):
    readings: List[Reading]