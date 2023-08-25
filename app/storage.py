from collections import defaultdict
from .models import DeviceReadings, Reading


class ReadingsStorage:
    """
    Singleton Reading Storage
    """
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.readings_db = defaultdict(dict)
        return cls._instance

    def _generate_key(self, reading:Reading) -> tuple:
        return (reading.timestamp, reading.count)

    def store_readings(self, readings_data: DeviceReadings) -> bool:
        readings = readings_data.readings
        device_id = readings_data.id

        for reading in readings:
            key = self._generate_key(reading)
            self.readings_db[device_id][key] = reading.model_dump()

        return device_id

    def fetch_readings(self, device_id):
        if device_id not in self.readings_db:
            return []
        
        return list(self.readings_db[device_id].values())

readings_storage = ReadingsStorage()
